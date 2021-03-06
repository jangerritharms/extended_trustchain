import src.communication.messages_pb2 as msg
from src.pyipv8.ipv8.attestation.trustchain.block import UNKNOWN_SEQ
from src.public_key import PublicKey


class BlockIndex(object):
    """The BlockIndex is one of the major components that enable the calculation of the state of the
    agent given their chain. The index shows for each public key, which blocks are recorded, either
    in an exchange or in the database itself. The entries of the index consists of tuples
    (public_key, [indices]), where the list of indices shows which sequence numbers of that public
    key are present. The sequence number given by "to" is also included in the range in contrast to
    the standard indexing in Python.
    """

    def __init__(self, entries=[]):
        """Creates a new BlockIndex and initializes the entries.

        Keyword Arguments:
            entries {[(PublicKey,[int])]} -- Initial entries of the BlockIndex
             (default: {[]})
        """

        self.entries = entries

    def get(self, public_key):
        """Get the indeces of a specific public key in this index
        
        Arguments:
            public_key {string} -- Binary public key
        """
        return next((index for key, index in self.entries if key == public_key), [])


    @classmethod
    def from_chain(cls, chain):
        """Calculates the index of a given chain.

        Arguments:
            chain {[Block]} -- Complete chain of another agent.
        """

        index_dict = {}
        for block in chain:
            index_dict.setdefault(block.public_key, []).append(block.sequence_number)
            if block.transaction.get('transfer_up') or block.transaction.get('transfer_down'):
                transfer = {}
                if block.link_sequence_number != UNKNOWN_SEQ:
                    transfer = block.transaction['transfer_up']
                else:
                    transfer = block.transaction['transfer_down']
                for elem in transfer:
                    index_dict.setdefault(elem[0].decode('hex'), []).extend(elem[1])

        return cls([(elem[0], sorted(list(set(elem[1])))) for elem in index_dict.items()])

    @classmethod
    def from_blocks(cls, blocks):
        """Calculates the index given all blocks that should be in the index e.g. from a database.

        Arguments:
            blocks {[Block]} -- All blocks that should be recorded in the index.
        """

        index_dict = {}
        for block in blocks:
            index_dict.setdefault(block.public_key, []).append(block.sequence_number)

        return cls([(elem[0], sorted(list(set(elem[1])))) for elem in index_dict.items()])

    @classmethod
    def from_message(cls, message):
        return cls([(entry.public_key, [num for num in entry.sequence_numbers])
                    for entry in message.entries])

    def __sub__(self, other):
        """Returns an index of the items which are in self but not in other.

        Arguments:
            other {BlockIndex} -- The index which shall be subtracted
        """

        own_index = sorted(self.entries, key=lambda x: x[0])
        other_index = sorted(other.entries, key=lambda x: x[0])

        i = 0
        j = 0
        exchange = []
        while i < len(own_index) and j < len(other_index):
            own_key = own_index[i][0]
            other_key = other_index[j][0]

            if own_key == other_key:
                if own_index[i][1] != other_index[j][1]:
                    diff = list(set(own_index[i][1]) - set(other_index[j][1]))
                    if len(diff) > 0:
                        exchange.append((own_key, diff))
                i += 1
                j += 1
            elif own_key < other_key:
                exchange.append((own_key, own_index[i][1]))
                i += 1
            else:
                j += 1

        while i < len(own_index):
            own_key = own_index[i][0]
            exchange.append((own_key, own_index[i][1]))
            i += 1

        return BlockIndex(exchange)

    def __add__(self, other):
        """Returns the union of both indexes.

        Arguments:
            other {BlockIndex} -- The index which shall be subtracted
        """

        own_index = sorted(self.entries, key=lambda x: x[0])
        other_index = sorted(other.entries, key=lambda x: x[0])

        i = 0
        j = 0
        exchange = []
        while i < len(own_index) and j < len(other_index):
            own_key = own_index[i][0]
            other_key = other_index[j][0]

            if own_key == other_key:
                union = list(set(own_index[i][1]) | set(other_index[j][1]))
                if len(union) > 0:
                    exchange.append((own_key, union))
                i += 1
                j += 1
            elif own_key < other_key:
                exchange.append((own_key, own_index[i][1]))
                i += 1
            else:
                exchange.append((other_key, other_index[j][1]))
                j += 1

        while i < len(own_index):
            own_key = own_index[i][0]
            exchange.append((own_key, own_index[i][1]))
            i += 1

        while j < len(other_index):
            other_key = other_index[j][0]
            exchange.append((other_key, other_index[j][1]))
            j += 1

        return BlockIndex(exchange)

    def as_message(self):
        """Creates a BlockIndex message from the given object.
        """
        message_entries = [msg.BlockIndexEntry(public_key=entry[0],
                                               sequence_numbers=entry[1]) for entry in self.entries]
        return msg.BlockIndex(entries=message_entries)

    def to_database_args(self):
        """Converts the entries to tuples of (public_key, sequence_number) entries for each single
        block. This is a convenience method for retrieving blocks from the database. For use with
        the database the public keys need to be converted to buffer objects.
        """

        return [(entry[0], seq) for entry in self.entries for seq in entry[1]]

    def db_pack(self):
        return [(entry[0].encode('hex'), entry[1]) for entry in self.entries]

    def __len__(self):
        return len(self.entries)
    
    def __str__(self):
        string = "BlockIndex {<"
        string += ">, <".join(["%s:%s" % (PublicKey.from_bin(elem[0]).as_readable(), elem[1])
                               for elem in self.entries])
        string += ">}"

        return string

    def remove(self, public_key):
        """Removes the entries for a specific agent identified by the public_key.
        
        Arguments:
            public_key {PublicKey} -- Public key of the agent to be removed from the index
        """
        self.entries = [entry for entry in self.entries if entry[0] != public_key.as_bin()]
