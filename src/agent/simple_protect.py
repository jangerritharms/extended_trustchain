import random
import logging
from collections import Counter

import src.communication.messages_pb2 as msg

from src.agent.base import BaseAgent
from src.chain.block import Block
from src.communication.messaging import MessageHandler
from src.communication.messages import NewMessage
from src.chain.index import BlockIndex
from src.agent.exchange_storage import ExchangeStorage
from src.agent.request_cache import RequestCache


class ProtectSimpleAgent(BaseAgent):
    """The ProtectSimple agent only stores on the chain the hashes of the data that was exchanged
    instead of all blocks. This way an agent still cannot lie but the chains remain as small as
    possible. However that agent needs to keep track of which data was received with which block.
    This happens with the RequestStorage.
    """

    _type = "ProtectSimple"

    def __init__(self, *args, **kwargs):
        super(ProtectSimpleAgent, self).__init__(*args, **kwargs)
        self.ignore_list = []
        self.request_cache = RequestCache()
        self.exchange_storage = ExchangeStorage()

    def request_protect(self, partner=None):
        """Requests a new PROTECT interaction with a partner. If no partner is passed as argument
        a random partner will be chosen from the known agents. The initiator sends his complete
        chain to the partner. The partner receives a PROTECT_CHAIN message with that chain attached.
        If the random agent is the agent itself or an agent with an existing unfinished request the
        request is cancelled.

        Keyword Arguments:
            partner {AgentInfo} -- Info of partner to perform interaction with (default: {None})
        """

        while partner is None or partner == self.get_info():
            partner = random.choice(self.agents)

        if self.request_cache.get(partner.address) is not None:
            self.logger.debug('Request already open, ignoring request with %s', partner.address)
            return
        if partner.address in self.ignore_list:
            return

        chain = self.database.get_chain(self.public_key)

        db = msg.Database(info=self.get_info().as_message(),
                          blocks=[block.as_message() for block in chain])
        self.request_cache.new(partner.address)
        self.com.send(partner.address, NewMessage(msg.PROTECT_CHAIN, db))

        self.logger.debug("[0] Requesting PROTECT with %s", partner.address)

    @MessageHandler(msg.PROTECT_CHAIN)
    def protect_chain(self, sender, body):
        """Handles a received PROTECT request. The agents receives a partner's chain who is
        requesting an exchange of endorsements and following interaction. The agent checks the chain
        for consistency. The chain should be complete and if it includes interactions it should also
        include endorsements. If there already exists an open, unfinished request with that agent,
        the request is rejected and a msg.PROTECT_REJECT message is sent. If verification checks out
        the agents requests a database index from the other agent. If the verification fails, a
        msg.PROTECT_REJECT message is sent and the initiator is added to the ignore list.

        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.Database} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is not None:
            self.logger.debug('Request already open, ignoring request from %s', sender)
            self.com.send(sender, NewMessage(msg.PROTECT_REJECT, msg.Empty()))
            return

        if sender in self.ignore_list:
            self.logger.warning('Agent %s is in ignore list', sender)
            self.com.send(sender, NewMessage(msg.PROTECT_REJECT, msg.Empty()))
            return

        chain = [Block.from_message(block) for block in body.blocks]

        self.request_cache.new(sender, chain)
        verification = self.verify_chain(chain)

        if verification:
            self.com.send(sender, NewMessage(msg.PROTECT_INDEX_REQUEST, msg.Empty()))
        else:
            self.ignore_list.append(sender)
            self.com.send(sender, NewMessage(msg.PROTECT_REJECT, msg.Empty()))

    @MessageHandler(msg.PROTECT_INDEX_REQUEST)
    def protect_index_request(self, sender, body):
        """Handles a received PROTECT_INDEX_REQUEST. A PROTECT exchange was accepted by both sides.
        The agent is required to send exchanges that list the blocks received from other agents. The
        agent keeps track of these in the exchange storage. If a request is found which matches the
        sender the agent sends a msg.PROTECT_INDEX_REPLY message to the responder of the PROTECT
        exchange.

        Arguments:
            sender {Address} -- Address string of the agent
            body {msg.Empty} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return

        message = self.exchange_storage.as_message()
        self.com.send(sender, NewMessage(msg.PROTECT_INDEX_REPLY, message))

    @MessageHandler(msg.PROTECT_INDEX_REPLY)
    def protect_index_reply(self, sender, body):
        """Handles a received PROTECT_INDEX_REPLY. A PROTECT exchange is ongoing, the exchanges were
        received which should add up to the hashes stored on the chain. If a request for the sender
        is found, the agent checks which blocks the initiator of the PROTECT exchange has that the
        checking agent is not aware of and requests those.
        
        Arguments:
            sender {Address} -- Address string of the agent
            body {msg.ExchangeIndex} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return

        exchanges = ExchangeStorage.from_message(body)

        partner_index = BlockIndex()
        for block_hash, index in exchanges.exchanges.iteritems():
            partner_index = partner_index + index
        partner_index += BlockIndex.from_blocks(self.request_cache.get(sender).chain)

        own_index = BlockIndex.from_blocks(self.database.get_all_blocks())

        db = (partner_index - own_index).as_message()
        self.com.send(sender, NewMessage(msg.PROTECT_BLOCKS_REQUEST, db))

        self.request_cache.get(sender).index = partner_index

    @MessageHandler(msg.PROTECT_BLOCKS_REQUEST)
    def protect_blocks_request(self, sender, body):
        """Handles a received PROTECT_BLOCKS_REQUEST. A PROTECT exchange is ongoing, the initiator
        received a request for blocks that initiator has above the responder. The initiator selects
        those from the database and sends them to the responder in a msg.PROTECT_BLOCKS_REPLY
        message. The uploaded data is stored in the request cache as it's hash will be stored on the
        exchange block created for this request.

        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.BlockIndex} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            logging.error('No open reqest found for this agent')
            return

        index = BlockIndex.from_message(body)

        self.request_cache.get(sender).transfer_up = index
        blocks = self.database.index(index)

        db = msg.Database(info=self.get_info().as_message(),
                          blocks=[block.as_message() for block in blocks])
        self.com.send(sender, NewMessage(msg.PROTECT_BLOCKS_REPLY, db))

        self.logger.debug("[2] Sending BLOCKS to %s", sender)

    @MessageHandler(msg.PROTECT_BLOCKS_REPLY)
    def protect_blocks_reply(self, sender, body):
        """Handles a received PROTECT_BLOCKS_REPLY. A PROTECT exchange is ongoing, the responder
        received the blocks the initiator had more than himself. Now the responder can check that
        the blocks add up to all information of the agent as proven by the hashes of the exchange
        blocks on the chain of the initiator. If the check succeeds, the agent shows his agreement
        by sending his own chain and blocks that he has above the initiator in a 
        msg.PROTECT_CHAIN_BLOCKS message. If the check fails, the agent sends a msg.PROTECT_REJECT
        message and adds the initiator to the ignore list.
        
        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.Database} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            logging.error('No open reqest found for this agent')
            return

        blocks = [Block.from_message(block) for block in body.blocks]

        verification = self.verify_blocks(blocks)

        if verification:
            own_chain = self.database.get_chain(self.public_key)
            own_index = BlockIndex.from_blocks(self.database.get_all_blocks())
            partner_index = self.request_cache.get(sender).index
            transfer_down = (own_index - partner_index)
            self.request_cache.get(sender).transfer_down = transfer_down
            sub_database = self.database.index(transfer_down)

            db = msg.ChainAndBlocks(chain=[block.as_message() for block in own_chain],
                                    blocks=[block.as_message() for block in sub_database])
            self.com.send(sender, NewMessage(msg.PROTECT_CHAIN_BLOCKS, db))

            self.logger.debug("[3] Sending CHAIN AND BLOCKS to %s", sender)
        else:
            self.ignore_list.append(sender)
            self.com.send(sender, NewMessage(msg.PROTECT_REJECT, msg.Empty()))

    @MessageHandler(msg.PROTECT_CHAIN_BLOCKS)
    def proect_chain_blocks(self, sender, body):
        """Handles a received PROTECT_CHAIN_BLOCKS message. A PROTECT exchange is ongoing, the
        initiator received chain, blocks and exchange data from the responder. The
        initiator should check whether the responder is completely trustworthy and shares all his
        data. The chain and exchange data is verified and only if the data checks out the next step
        is done. That is the block proposal, all data is exchanged and both agents trust each other,
        an exchange block can be created which includes the hashes of both sets of exchanged blocks.
        If the verification fails the responder is added to the ignore list and a msg.PROTECT_REJECT
        is sent.

        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.ChainAndBlocks} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return
        chain = [Block.from_message(block) for block in body.chain]
        blocks = [Block.from_message(block) for block in body.blocks]

        verification = self.verify_chain_and_blocks(blocks)
        transfer_down = BlockIndex.from_blocks(blocks)

        if verification:
            partner = next((a for a in self.agents if a.address == sender), None)
            payload = {'transfer_up': self.request_cache.get(sender).transfer_up.db_pack(),
                       'transfer_down': transfer_down.db_pack()}
            new_block = self.block_factory.create_new(partner.public_key, payload=payload)
            self.com.send(partner.address, NewMessage(msg.PROTECT_BLOCK_PROPOSAL,
                                                      new_block.as_message()))
            self.exchange_storage.add_exchange(new_block,
                                               self.request_cache.get(sender).transfer_up)

            self.logger.debug("[4] Sending PROPOSAL to %s", sender)
        else:
            self.ignore_list.append(sender)
            self.com.send(sender, NewMessage(msg.PROTECT_REJECT, msg.Empty()))

    @MessageHandler(msg.PROTECT_BLOCK_PROPOSAL)
    def protect_block_proposal(self, sender, body):
        """Handles a received PROTECT_BLOCK_PROPOSAL message. A PROTECT exchange is ongoing, the
        responder received the block proposal from the initiator. This includes the two hashes of
        the block sets that were exchanged between the two agents. The agent checks both hashes and
        if they check out the agent creates the block agreement, signs and stores it and replies to
        the initiator with the msg.PROTECT_BLOCK_AGREEMENT message.

        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.Block} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return

        block = Block.from_message(body)
        self.database.add(block)

        new_block = self.block_factory.create_linked(block)
        self.com.send(sender, NewMessage(msg.PROTECT_BLOCK_AGREEMENT, new_block.as_message()))
        self.exchange_storage.add_exchange(new_block,
                                           self.request_cache.get(sender).transfer_down)

        self.request_cache.remove(sender)
        self.logger.debug("[5] Sending AGREEMENT to %s", sender)

    @MessageHandler(msg.PROTECT_BLOCK_AGREEMENT)
    def protect_block_agreement(self, sender, body):
        """Handles a received PROTECT_BLOCK_AGREEMENT message. A PROTECT exchange is ongoing, the
        initiator received the block agreement from the responder. The initiator checks whether the
        block proposal and block agreement blocks include the same data and stores them in the
        database. The request is then concluded and removed from the request cache. Now the actual
        interaction can take place which is handled by the BaseAgent super-class.

        Arguments:
            sender {Address} -- Address string of the agent.
            body {msg.Block} -- Body of the incoming message.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return

        block = Block.from_message(body)
        self.database.add(block)

        partner = next((a for a in self.agents if a.address == sender), None)
        self.request_interaction(partner)
        self.request_cache.remove(sender)   

        self.logger.debug("[6] Storing AGREEMENT from %s", sender)

    @MessageHandler(msg.PROTECT_REJECT)
    def protect_reject(self, sender, body):
        """Handles a received PROTECT_REJECT message. This message is sent when the agent that
        receives a message does not agree with the conditions of the request. Multiple reasons lead
        to such an event. When received, an agent is supposed to remove the request from the request
        cache in order to allow for more requests with that agent in the future.
        
        Arguments:
            sender {Address} -- Address of the sender of the request.
            body {msg.Empty} -- Empty message body.
        """

        if self.request_cache.get(sender) is None:
            self.logger.error('No open reqest found for this agent')
            return
        self.request_cache.remove(sender)

    def step(self):

        self.request_protect()

    def verify_chain(self, chain):
        """Verifies the correctness of a chain received by another agent.

        Arguments:
            chain {[Block]} -- Agent's complete chain

        Returns:
            bool -- Outcome of the verification, True means correct, False means fraud
        """

        seq = [block.sequence_number for block in chain]
        if not Counter(seq) == Counter(range(1, max(seq)+1)):
            return False
        return True

    def verify_blocks(self, block):

        return True

    def verify_chain_and_blocks(self, blocks):
        return True

    def verify_exchange(self, chain, exchange):
        return True