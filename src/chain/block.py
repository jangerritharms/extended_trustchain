import pickle
import time

import src.communication.messages_pb2 as msg

from src.pyipv8.ipv8.attestation.trustchain.block import TrustChainBlock, GENESIS_HASH, EMPTY_SIG, \
    EMPTY_PK, GENESIS_SEQ, UNKNOWN_SEQ
from src.pyipv8.ipv8.messaging.serialization import Serializer



class Block(TrustChainBlock):
    """Extension to the normal TrustChainBlock, mostly for convenience to conver blocks to
    messages and back.
    """

    def __init__(self, data=None, serializer=Serializer()):
        if data is None:
            # data
            self.transaction = {}
            # identity
            self.public_key = EMPTY_PK
            self.sequence_number = GENESIS_SEQ
            # linked identity
            self.link_public_key = EMPTY_PK
            self.link_sequence_number = UNKNOWN_SEQ
            # validation
            self.previous_hash = GENESIS_HASH
            self.signature = EMPTY_SIG
            # debug stuff
            self.insert_time = None
        else:
            self.transaction = data[0]
            (self.public_key, self.sequence_number, self.link_public_key, self.link_sequence_number,
             self.previous_hash, self.signature, self.insert_time) = (
                data[1], data[2], data[3], data[4], data[5], data[6], data[7])
            if isinstance(self.public_key, buffer):
                self.public_key = str(self.public_key)
            if isinstance(self.link_public_key, buffer):
                self.link_public_key = str(self.link_public_key)
            if isinstance(self.previous_hash, buffer):
                self.previous_hash = str(self.previous_hash)
            if isinstance(self.signature, buffer):
                self.signature = str(self.signature)
        self.serializer = serializer

    def as_message(self):
        """Convert a Block to a message to send to other agents.

        Returns:
            msg.Block -- Block message describing the block instance.
        """
        return msg.Block(
            payload=pickle.dumps(self.transaction),
            public_key=self.public_key,
            sequence_number=self.sequence_number,
            link_public_key=self.link_public_key,
            link_sequence_number=self.link_sequence_number,
            previous_hash=self.previous_hash,
            signature=self.signature
        )

    @classmethod
    def from_message(cls, message):
        """Creats a block from a block message.

        Arguments:
            message {msg.Block} -- Block message describing the block to be created.
        """

        return cls([
            pickle.loads(message.payload),
            message.public_key,
            message.sequence_number,
            message.link_public_key,
            message.link_sequence_number,
            message.previous_hash,
            message.signature,
            time.time()
        ])

    @classmethod
    def convert_to_Block(cls, obj):
        """Converts TrustChainBlocks to Blocks.
        
        Arguments:
            obj {TrustChainBlock} -- Block that will be converted
        """

        obj.__class__ = Block
        return obj