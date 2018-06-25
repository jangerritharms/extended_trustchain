# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/communication/messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/communication/messages.proto',
  package='',
  serialized_pb=_b('\n src/communication/messages.proto\"\x07\n\x05\x45mpty\">\n\tAgentInfo\x12\x12\n\npublic_key\x18\x01 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\"%\n\x08Register\x12\x19\n\x05\x61gent\x18\x01 \x02(\x0b\x32\n.AgentInfo\"\'\n\nUnregister\x12\x19\n\x05\x61gent\x18\x01 \x02(\x0b\x32\n.AgentInfo\"(\n\nAgentReply\x12\x1a\n\x06\x61gents\x18\x01 \x03(\x0b\x32\n.AgentInfo\"\xd8\x02\n\x0eWrapperMessage\x12\x13\n\x04type\x18\x01 \x02(\x0e\x32\x05.Type\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\x12\x17\n\x05\x65mpty\x18\n \x01(\x0b\x32\x06.EmptyH\x00\x12\x1d\n\x08register\x18\x0b \x01(\x0b\x32\t.RegisterH\x00\x12\"\n\x0b\x61gent_reply\x18\x0c \x01(\x0b\x32\x0b.AgentReplyH\x00\x12!\n\nunregister\x18\r \x01(\x0b\x32\x0b.UnregisterH\x00\x12\x17\n\x05\x62lock\x18\x0e \x01(\x0b\x32\x06.BlockH\x00\x12\x17\n\x02\x64\x62\x18\x0f \x01(\x0b\x32\t.DatabaseH\x00\x12\x1c\n\x05index\x18\x10 \x01(\x0b\x32\x0b.BlockIndexH\x00\x12&\n\x0b\x63hain_index\x18\x11 \x01(\x0b\x32\x0f.ChainAndBlocksH\x00\x12\"\n\x08\x65x_index\x18\x12 \x01(\x0b\x32\x0e.ExchangeIndexH\x00\x42\x05\n\x03msg\"\xb4\x01\n\x05\x42lock\x12\x0f\n\x07payload\x18\x01 \x02(\x0c\x12\x12\n\npublic_key\x18\x02 \x02(\x0c\x12\x17\n\x0fsequence_number\x18\x03 \x02(\x05\x12\x17\n\x0flink_public_key\x18\x04 \x02(\x0c\x12\x1c\n\x14link_sequence_number\x18\x05 \x02(\x05\x12\x15\n\rprevious_hash\x18\x06 \x02(\x0c\x12\x11\n\tsignature\x18\x07 \x02(\x0c\x12\x0c\n\x04hash\x18\x08 \x01(\x0c\"<\n\x08\x44\x61tabase\x12\x18\n\x04info\x18\x01 \x02(\x0b\x32\n.AgentInfo\x12\x16\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x06.Block\"D\n\x12\x45xchangeIndexEntry\x12\x12\n\nblock_hash\x18\x01 \x02(\x0c\x12\x1a\n\x05index\x18\x02 \x02(\x0b\x32\x0b.BlockIndex\"5\n\rExchangeIndex\x12$\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x13.ExchangeIndexEntry\"?\n\x0f\x42lockIndexEntry\x12\x12\n\npublic_key\x18\x01 \x02(\x0c\x12\x18\n\x10sequence_numbers\x18\x02 \x03(\x05\"/\n\nBlockIndex\x12!\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x10.BlockIndexEntry\"a\n\x0e\x43hainAndBlocks\x12\x15\n\x05\x63hain\x18\x01 \x03(\x0b\x32\x06.Block\x12\x16\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x06.Block\x12 \n\x08\x65xchange\x18\x03 \x02(\x0b\x32\x0e.ExchangeIndex*\xd5\x02\n\x04Type\x12\x0c\n\x08REGISTER\x10\x01\x12\x0f\n\x0b\x41GENT_REPLY\x10\x02\x12\x11\n\rAGENT_REQUEST\x10\x03\x12\x0e\n\nUNREGISTER\x10\x04\x12\x12\n\x0e\x42LOCK_PROPOSAL\x10\x05\x12\x13\n\x0f\x42LOCK_AGREEMENT\x10\x06\x12\x11\n\rPROTECT_CHAIN\x10\x07\x12\x1a\n\x16PROTECT_BLOCKS_REQUEST\x10\x08\x12\x18\n\x14PROTECT_BLOCKS_REPLY\x10\t\x12\x18\n\x14PROTECT_CHAIN_BLOCKS\x10\n\x12\x1a\n\x16PROTECT_BLOCK_PROPOSAL\x10\x0b\x12\x1b\n\x17PROTECT_BLOCK_AGREEMENT\x10\x0c\x12\x12\n\x0ePROTECT_REJECT\x10\r\x12\x19\n\x15PROTECT_INDEX_REQUEST\x10\x0e\x12\x17\n\x13PROTECT_INDEX_REPLY\x10\x0f')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_REPLY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_REQUEST', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK_PROPOSAL', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK_AGREEMENT', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_CHAIN', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_BLOCKS_REQUEST', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_BLOCKS_REPLY', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_CHAIN_BLOCKS', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_BLOCK_PROPOSAL', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_BLOCK_AGREEMENT', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_REJECT', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_INDEX_REQUEST', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTECT_INDEX_REPLY', index=14, number=15,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1162,
  serialized_end=1503,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
REGISTER = 1
AGENT_REPLY = 2
AGENT_REQUEST = 3
UNREGISTER = 4
BLOCK_PROPOSAL = 5
BLOCK_AGREEMENT = 6
PROTECT_CHAIN = 7
PROTECT_BLOCKS_REQUEST = 8
PROTECT_BLOCKS_REPLY = 9
PROTECT_CHAIN_BLOCKS = 10
PROTECT_BLOCK_PROPOSAL = 11
PROTECT_BLOCK_AGREEMENT = 12
PROTECT_REJECT = 13
PROTECT_INDEX_REQUEST = 14
PROTECT_INDEX_REPLY = 15



_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=43,
)


_AGENTINFO = _descriptor.Descriptor(
  name='AgentInfo',
  full_name='AgentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='AgentInfo.public_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='AgentInfo.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='AgentInfo.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=107,
)


_REGISTER = _descriptor.Descriptor(
  name='Register',
  full_name='Register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent', full_name='Register.agent', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=146,
)


_UNREGISTER = _descriptor.Descriptor(
  name='Unregister',
  full_name='Unregister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent', full_name='Unregister.agent', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=187,
)


_AGENTREPLY = _descriptor.Descriptor(
  name='AgentReply',
  full_name='AgentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='AgentReply.agents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=229,
)


_WRAPPERMESSAGE = _descriptor.Descriptor(
  name='WrapperMessage',
  full_name='WrapperMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='WrapperMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='WrapperMessage.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='empty', full_name='WrapperMessage.empty', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register', full_name='WrapperMessage.register', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_reply', full_name='WrapperMessage.agent_reply', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unregister', full_name='WrapperMessage.unregister', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='WrapperMessage.block', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='db', full_name='WrapperMessage.db', index=7,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='WrapperMessage.index', index=8,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chain_index', full_name='WrapperMessage.chain_index', index=9,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ex_index', full_name='WrapperMessage.ex_index', index=10,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='WrapperMessage.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=232,
  serialized_end=576,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='Block.payload', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Block.public_key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='Block.sequence_number', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_public_key', full_name='Block.link_public_key', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_sequence_number', full_name='Block.link_sequence_number', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='Block.previous_hash', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Block.signature', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Block.hash', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=759,
)


_DATABASE = _descriptor.Descriptor(
  name='Database',
  full_name='Database',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='Database.info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='Database.blocks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=821,
)


_EXCHANGEINDEXENTRY = _descriptor.Descriptor(
  name='ExchangeIndexEntry',
  full_name='ExchangeIndexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='ExchangeIndexEntry.block_hash', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ExchangeIndexEntry.index', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=823,
  serialized_end=891,
)


_EXCHANGEINDEX = _descriptor.Descriptor(
  name='ExchangeIndex',
  full_name='ExchangeIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='ExchangeIndex.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=893,
  serialized_end=946,
)


_BLOCKINDEXENTRY = _descriptor.Descriptor(
  name='BlockIndexEntry',
  full_name='BlockIndexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='BlockIndexEntry.public_key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_numbers', full_name='BlockIndexEntry.sequence_numbers', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=948,
  serialized_end=1011,
)


_BLOCKINDEX = _descriptor.Descriptor(
  name='BlockIndex',
  full_name='BlockIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='BlockIndex.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1060,
)


_CHAINANDBLOCKS = _descriptor.Descriptor(
  name='ChainAndBlocks',
  full_name='ChainAndBlocks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain', full_name='ChainAndBlocks.chain', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='ChainAndBlocks.blocks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='ChainAndBlocks.exchange', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1159,
)

_REGISTER.fields_by_name['agent'].message_type = _AGENTINFO
_UNREGISTER.fields_by_name['agent'].message_type = _AGENTINFO
_AGENTREPLY.fields_by_name['agents'].message_type = _AGENTINFO
_WRAPPERMESSAGE.fields_by_name['type'].enum_type = _TYPE
_WRAPPERMESSAGE.fields_by_name['empty'].message_type = _EMPTY
_WRAPPERMESSAGE.fields_by_name['register'].message_type = _REGISTER
_WRAPPERMESSAGE.fields_by_name['agent_reply'].message_type = _AGENTREPLY
_WRAPPERMESSAGE.fields_by_name['unregister'].message_type = _UNREGISTER
_WRAPPERMESSAGE.fields_by_name['block'].message_type = _BLOCK
_WRAPPERMESSAGE.fields_by_name['db'].message_type = _DATABASE
_WRAPPERMESSAGE.fields_by_name['index'].message_type = _BLOCKINDEX
_WRAPPERMESSAGE.fields_by_name['chain_index'].message_type = _CHAINANDBLOCKS
_WRAPPERMESSAGE.fields_by_name['ex_index'].message_type = _EXCHANGEINDEX
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['empty'])
_WRAPPERMESSAGE.fields_by_name['empty'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['register'])
_WRAPPERMESSAGE.fields_by_name['register'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['agent_reply'])
_WRAPPERMESSAGE.fields_by_name['agent_reply'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['unregister'])
_WRAPPERMESSAGE.fields_by_name['unregister'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['block'])
_WRAPPERMESSAGE.fields_by_name['block'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['db'])
_WRAPPERMESSAGE.fields_by_name['db'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['index'])
_WRAPPERMESSAGE.fields_by_name['index'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['chain_index'])
_WRAPPERMESSAGE.fields_by_name['chain_index'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_WRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _WRAPPERMESSAGE.fields_by_name['ex_index'])
_WRAPPERMESSAGE.fields_by_name['ex_index'].containing_oneof = _WRAPPERMESSAGE.oneofs_by_name['msg']
_DATABASE.fields_by_name['info'].message_type = _AGENTINFO
_DATABASE.fields_by_name['blocks'].message_type = _BLOCK
_EXCHANGEINDEXENTRY.fields_by_name['index'].message_type = _BLOCKINDEX
_EXCHANGEINDEX.fields_by_name['entries'].message_type = _EXCHANGEINDEXENTRY
_BLOCKINDEX.fields_by_name['entries'].message_type = _BLOCKINDEXENTRY
_CHAINANDBLOCKS.fields_by_name['chain'].message_type = _BLOCK
_CHAINANDBLOCKS.fields_by_name['blocks'].message_type = _BLOCK
_CHAINANDBLOCKS.fields_by_name['exchange'].message_type = _EXCHANGEINDEX
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['AgentInfo'] = _AGENTINFO
DESCRIPTOR.message_types_by_name['Register'] = _REGISTER
DESCRIPTOR.message_types_by_name['Unregister'] = _UNREGISTER
DESCRIPTOR.message_types_by_name['AgentReply'] = _AGENTREPLY
DESCRIPTOR.message_types_by_name['WrapperMessage'] = _WRAPPERMESSAGE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Database'] = _DATABASE
DESCRIPTOR.message_types_by_name['ExchangeIndexEntry'] = _EXCHANGEINDEXENTRY
DESCRIPTOR.message_types_by_name['ExchangeIndex'] = _EXCHANGEINDEX
DESCRIPTOR.message_types_by_name['BlockIndexEntry'] = _BLOCKINDEXENTRY
DESCRIPTOR.message_types_by_name['BlockIndex'] = _BLOCKINDEX
DESCRIPTOR.message_types_by_name['ChainAndBlocks'] = _CHAINANDBLOCKS
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

AgentInfo = _reflection.GeneratedProtocolMessageType('AgentInfo', (_message.Message,), dict(
  DESCRIPTOR = _AGENTINFO,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:AgentInfo)
  ))
_sym_db.RegisterMessage(AgentInfo)

Register = _reflection.GeneratedProtocolMessageType('Register', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:Register)
  ))
_sym_db.RegisterMessage(Register)

Unregister = _reflection.GeneratedProtocolMessageType('Unregister', (_message.Message,), dict(
  DESCRIPTOR = _UNREGISTER,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:Unregister)
  ))
_sym_db.RegisterMessage(Unregister)

AgentReply = _reflection.GeneratedProtocolMessageType('AgentReply', (_message.Message,), dict(
  DESCRIPTOR = _AGENTREPLY,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:AgentReply)
  ))
_sym_db.RegisterMessage(AgentReply)

WrapperMessage = _reflection.GeneratedProtocolMessageType('WrapperMessage', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPERMESSAGE,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:WrapperMessage)
  ))
_sym_db.RegisterMessage(WrapperMessage)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)

Database = _reflection.GeneratedProtocolMessageType('Database', (_message.Message,), dict(
  DESCRIPTOR = _DATABASE,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:Database)
  ))
_sym_db.RegisterMessage(Database)

ExchangeIndexEntry = _reflection.GeneratedProtocolMessageType('ExchangeIndexEntry', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEINDEXENTRY,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeIndexEntry)
  ))
_sym_db.RegisterMessage(ExchangeIndexEntry)

ExchangeIndex = _reflection.GeneratedProtocolMessageType('ExchangeIndex', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEINDEX,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeIndex)
  ))
_sym_db.RegisterMessage(ExchangeIndex)

BlockIndexEntry = _reflection.GeneratedProtocolMessageType('BlockIndexEntry', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKINDEXENTRY,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:BlockIndexEntry)
  ))
_sym_db.RegisterMessage(BlockIndexEntry)

BlockIndex = _reflection.GeneratedProtocolMessageType('BlockIndex', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKINDEX,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:BlockIndex)
  ))
_sym_db.RegisterMessage(BlockIndex)

ChainAndBlocks = _reflection.GeneratedProtocolMessageType('ChainAndBlocks', (_message.Message,), dict(
  DESCRIPTOR = _CHAINANDBLOCKS,
  __module__ = 'src.communication.messages_pb2'
  # @@protoc_insertion_point(class_scope:ChainAndBlocks)
  ))
_sym_db.RegisterMessage(ChainAndBlocks)


# @@protoc_insertion_point(module_scope)
