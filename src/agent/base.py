import os
import random
import time
import pickle

from tornado import ioloop

import src.communication.messages_pb2 as msg

from src.pyipv8.ipv8.keyvault.crypto import ECCrypto
from src.pyipv8.ipv8.attestation.trustchain.payload import HalfBlockPairPayload
from src.pyipv8.ipv8.messaging.serialization import Serializer
from src.pyipv8.ipv8.attestation.trustchain.block import TrustChainBlock
from src.public_key import PublicKey
from src.database import Database
from src.chain.block import Block
from src.chain.block_factory import BlockFactory
from src.agent.info import AgentInfo
from src.communication.interface import CommunicationInterface
from src.communication.messages import Message, MessageTypes, NewMessage
from src.communication.messaging import MessageProcessor, MessageHandler


class BaseAgent(MessageProcessor):
    """The BaseAgent class defines the default honest behavior for agents and includes all the
    attributes and functions to properly interact with the network, including the public and private
    keys, the communication interface and block creation tools. Also some default message handlers
    for replying to blocks, registering and unregistering are included.
    """

    def __init__(self):
        """Creates a new BaseAgent, creates keys and declares class attributes.
        """
        self.agents = []

        self.options = {}

        self.private_key = ECCrypto().generate_key('curve25519')
        self.public_key = PublicKey(self.private_key.pub())

        self.com = CommunicationInterface()
        self.database = None
        self.block_factory = None
        self.serializer = Serializer()

    def setup(self, options, port):
        """Loads a configuration for the agent. The configuration includes the discovery server
        address and experiment settings like the duration of the experiment. Also initializes
        components which depend on the configuration of this particular agent.

        Arguments:
            options {ExperimentOptions} -- Options for the Experiment
            port {unsinged int} -- Port for the receiver of the agent
        """

        self.options['duration'] = options['emulation_duration']
        self.options['startup_time'] = options['startup_time']
        self.options['discovery_server'] = 'tcp://localhost:' + str(options['discovery_port'])

        self.database = Database('', 'db_' + str(port))
        self.block_factory = BlockFactory(self.database, self.public_key, self.private_key)
        self.block_factory.create_genesis()

        self.com.configure(port)

    def get_info(self):
        """Return information about the agent.

        Returns:
            AgentInfo -- Info object about the agent.
        """

        return AgentInfo.from_agent(self)

    def request_interaction(self, partner=None):
        """Sends a block proposal to another known agent.

        Keyword Arguments:
            partner {AgentInfo} -- Contact information about the partner for the new interaction. If
            this is None, a partner will be selected randomly. (default: {None})
        """

        while partner is None or partner == self.get_info():
            partner = random.choice(self.agents)

        new_block = self.block_factory.create_new(partner.public_key)
        self.com.send(partner.address, NewMessage(msg.BLOCK_PROPOSAL,
                                                  new_block.as_message()))

    def request_agents(self):
        """Send a request for agents to the discovery server.
        """

        self.com.send(self.options['discovery_server'],
                      NewMessage(msg.AGENT_REQUEST, msg.Empty()))

    @MessageHandler(msg.AGENT_REPLY)
    def set_agents(self, sender, body):
        """Message handler for the AGENT_REPLY message which the agent receives in reply to the
        AGENT_REQUEST message. Set the list of known agents to the list of AgentInfo objects
        contained in the reply.

        Arguments:
            sender {string} -- Address string of the sender of the reply
            body {msg.AgentReply} -- AgentReply message, containing a list of AgentInfo objects
        """

        self.agents = [AgentInfo.from_message(agent) for agent in body.agents]

    @MessageHandler(msg.BLOCK_PROPOSAL)
    def block_proposal(self, sender, body):
        """Message handler for the BLOCK_PROPOSAL message which the agent receives from another
        agent that wants to create a record of a transaction. This function stores the block
        contained in the message and replies to the agent with an agreement block.

        Arguments:
            sender {string} -- Address string of the sender of the block proposal
            body {msg.Block} -- Block message describing the block proposal
        """

        block = Block.from_message(body)
        self.database.add(block)

        new_block = self.block_factory.create_linked(block)
        self.com.send(sender, NewMessage(msg.BLOCK_AGREEMENT, new_block.as_message()))

    @MessageHandler(msg.BLOCK_AGREEMENT)
    def block_confirm(self, sender, body):
        """Message handler for the BLOCK_AGREEMENT message which the agent receives from another
        agent in reply to a previous block proposal. This function simply stores that block.

        Arguments:
            sender {string} -- Address of the sender of the agreement block
            body {msg.Block} -- Block message describing the agreement block
        """

        block = Block.from_message(body)

        self.database.add(block)

    def register(self):
        """Sends a registration message to the discovery server with the agent's contact info. This
        announces to the network that the agent is available for interactions.
        """

        message = msg.Register(agent=self.get_info().as_message())
        self.com.send(self.options['discovery_server'], NewMessage(msg.REGISTER, message))

    def unregister(self):
        """Sends a unregistration message to the discovery server with the agent's contact info.
        This announces to the network that the agent is about to leave the network.
        """

        message = msg.Unregister(agent=self.get_info().as_message())
        self.com.send(self.options['discovery_server'], NewMessage(msg.UNREGISTER, message))
        time.sleep(1)
        self.loop.stop()

    def step(self):
        """Defines the behavior of the agent. This function is called every 0.01 seconds. Each call
        the agent decides according to some strategy whether to perform an action or not.
        """

        self.request_interaction()

    def write_data(self):
        """Serializes the state(database) of the agent in order to be analyzed afterwards. The files
        are stored in the `data/` directory and are called after the human readable form of the
        agents public key.
        """

        blocks = self.database._getall('', ())
        with open(os.path.join('data', self.public_key.as_readable() + '.dat'), 'wb') as f:
            database = msg.Database(info=self.get_info().as_message(),
                                    blocks=[block.as_message() for block in blocks])
            f.write(database.SerializeToString())

    def run(self):
        """
        Starts the main loop of the agent.
        """
        self.com.start(self.handle)

        self.register()

        self.loop = ioloop.IOLoop.current()
        self.loop.call_later(self.options['duration'], self.unregister)
        self.loop.call_later(self.options['startup_time'], self.request_agents)
        cb_step = ioloop.PeriodicCallback(self.step, 1000)
        self.loop.call_later(self.options['startup_time'] + 5, cb_step.start)
        self.loop.start()

        self.write_data()
