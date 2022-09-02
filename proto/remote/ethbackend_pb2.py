# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote/ethbackend.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.types import types_pb2 as types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17remote/ethbackend.proto\x12\x06remote\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11types/types.proto\"\x12\n\x10\x45therbaseRequest\".\n\x0e\x45therbaseReply\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\"\x13\n\x11NetVersionRequest\"\x1d\n\x0fNetVersionReply\x12\n\n\x02id\x18\x01 \x01(\x04\"\x15\n\x13NetPeerCountRequest\"\"\n\x11NetPeerCountReply\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\",\n\x17\x45ngineGetPayloadRequest\x12\x11\n\tpayloadId\x18\x01 \x01(\x04\"z\n\x13\x45nginePayloadStatus\x12$\n\x06status\x18\x01 \x01(\x0e\x32\x14.remote.EngineStatus\x12$\n\x0flatestValidHash\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12\x17\n\x0fvalidationError\x18\x03 \x01(\t\"y\n\x17\x45nginePayloadAttributes\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x1f\n\nprevRandao\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12*\n\x15suggestedFeeRecipient\x18\x03 \x01(\x0b\x32\x0b.types.H160\"\x88\x01\n\x15\x45ngineForkChoiceState\x12\"\n\rheadBlockHash\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\"\n\rsafeBlockHash\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12\'\n\x12\x66inalizedBlockHash\x18\x03 \x01(\x0b\x32\x0b.types.H256\"\x94\x01\n\x1e\x45ngineForkChoiceUpdatedRequest\x12\x36\n\x0f\x66orkchoiceState\x18\x01 \x01(\x0b\x32\x1d.remote.EngineForkChoiceState\x12:\n\x11payloadAttributes\x18\x02 \x01(\x0b\x32\x1f.remote.EnginePayloadAttributes\"e\n\x1c\x45ngineForkChoiceUpdatedReply\x12\x32\n\rpayloadStatus\x18\x01 \x01(\x0b\x32\x1b.remote.EnginePayloadStatus\x12\x11\n\tpayloadId\x18\x02 \x01(\x04\"\x18\n\x16ProtocolVersionRequest\"\"\n\x14ProtocolVersionReply\x12\n\n\x02id\x18\x01 \x01(\x04\"\x16\n\x14\x43lientVersionRequest\"&\n\x12\x43lientVersionReply\x12\x10\n\x08nodeName\x18\x01 \x01(\t\"/\n\x10SubscribeRequest\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.remote.Event\";\n\x0eSubscribeReply\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.remote.Event\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"y\n\x11LogsFilterRequest\x12\x14\n\x0c\x61llAddresses\x18\x01 \x01(\x08\x12\x1e\n\taddresses\x18\x02 \x03(\x0b\x32\x0b.types.H160\x12\x11\n\tallTopics\x18\x03 \x01(\x08\x12\x1b\n\x06topics\x18\x04 \x03(\x0b\x32\x0b.types.H256\"\xf5\x01\n\x12SubscribeLogsReply\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x1e\n\tblockHash\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12\x13\n\x0b\x62lockNumber\x18\x03 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x10\n\x08logIndex\x18\x05 \x01(\x04\x12\x1b\n\x06topics\x18\x06 \x03(\x0b\x32\x0b.types.H256\x12$\n\x0ftransactionHash\x18\x07 \x01(\x0b\x32\x0b.types.H256\x12\x18\n\x10transactionIndex\x18\x08 \x01(\x04\x12\x0f\n\x07removed\x18\t \x01(\x08\"C\n\x0c\x42lockRequest\x12\x13\n\x0b\x62lockHeight\x18\x02 \x01(\x04\x12\x1e\n\tblockHash\x18\x03 \x01(\x0b\x32\x0b.types.H256\"/\n\nBlockReply\x12\x10\n\x08\x62lockRlp\x18\x01 \x01(\x0c\x12\x0f\n\x07senders\x18\x02 \x01(\x0c\"0\n\x10TxnLookupRequest\x12\x1c\n\x07txnHash\x18\x01 \x01(\x0b\x32\x0b.types.H256\"%\n\x0eTxnLookupReply\x12\x13\n\x0b\x62lockNumber\x18\x01 \x01(\x04\"!\n\x10NodesInfoRequest\x12\r\n\x05limit\x18\x01 \x01(\r\"9\n\x0eNodesInfoReply\x12\'\n\tnodesInfo\x18\x01 \x03(\x0b\x32\x14.types.NodeInfoReply\",\n\nPeersReply\x12\x1e\n\x05peers\x18\x01 \x03(\x0b\x32\x0f.types.PeerInfo\"%\n\x11PendingBlockReply\x12\x10\n\x08\x62lockRlp\x18\x01 \x01(\x0c*J\n\x05\x45vent\x12\n\n\x06HEADER\x10\x00\x12\x10\n\x0cPENDING_LOGS\x10\x01\x12\x11\n\rPENDING_BLOCK\x10\x02\x12\x10\n\x0cNEW_SNAPSHOT\x10\x03*Y\n\x0c\x45ngineStatus\x12\t\n\x05VALID\x10\x00\x12\x0b\n\x07INVALID\x10\x01\x12\x0b\n\x07SYNCING\x10\x02\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x03\x12\x16\n\x12INVALID_BLOCK_HASH\x10\x04\x32\xe5\x08\n\nETHBACKEND\x12=\n\tEtherbase\x12\x18.remote.EtherbaseRequest\x1a\x16.remote.EtherbaseReply\x12@\n\nNetVersion\x12\x19.remote.NetVersionRequest\x1a\x17.remote.NetVersionReply\x12\x46\n\x0cNetPeerCount\x12\x1b.remote.NetPeerCountRequest\x1a\x19.remote.NetPeerCountReply\x12N\n\x12\x45ngineGetPayloadV1\x12\x1f.remote.EngineGetPayloadRequest\x1a\x17.types.ExecutionPayload\x12J\n\x12\x45ngineNewPayloadV1\x12\x17.types.ExecutionPayload\x1a\x1b.remote.EnginePayloadStatus\x12i\n\x19\x45ngineForkChoiceUpdatedV1\x12&.remote.EngineForkChoiceUpdatedRequest\x1a$.remote.EngineForkChoiceUpdatedReply\x12\x36\n\x07Version\x12\x16.google.protobuf.Empty\x1a\x13.types.VersionReply\x12O\n\x0fProtocolVersion\x12\x1e.remote.ProtocolVersionRequest\x1a\x1c.remote.ProtocolVersionReply\x12I\n\rClientVersion\x12\x1c.remote.ClientVersionRequest\x1a\x1a.remote.ClientVersionReply\x12?\n\tSubscribe\x12\x18.remote.SubscribeRequest\x1a\x16.remote.SubscribeReply0\x01\x12J\n\rSubscribeLogs\x12\x19.remote.LogsFilterRequest\x1a\x1a.remote.SubscribeLogsReply(\x01\x30\x01\x12\x31\n\x05\x42lock\x12\x14.remote.BlockRequest\x1a\x12.remote.BlockReply\x12=\n\tTxnLookup\x12\x18.remote.TxnLookupRequest\x1a\x16.remote.TxnLookupReply\x12<\n\x08NodeInfo\x12\x18.remote.NodesInfoRequest\x1a\x16.remote.NodesInfoReply\x12\x33\n\x05Peers\x12\x16.google.protobuf.Empty\x1a\x12.remote.PeersReply\x12\x41\n\x0cPendingBlock\x12\x16.google.protobuf.Empty\x1a\x19.remote.PendingBlockReplyB\x11Z\x0f./remote;remoteb\x06proto3')

_EVENT = DESCRIPTOR.enum_types_by_name['Event']
Event = enum_type_wrapper.EnumTypeWrapper(_EVENT)
_ENGINESTATUS = DESCRIPTOR.enum_types_by_name['EngineStatus']
EngineStatus = enum_type_wrapper.EnumTypeWrapper(_ENGINESTATUS)
HEADER = 0
PENDING_LOGS = 1
PENDING_BLOCK = 2
NEW_SNAPSHOT = 3
VALID = 0
INVALID = 1
SYNCING = 2
ACCEPTED = 3
INVALID_BLOCK_HASH = 4


_ETHERBASEREQUEST = DESCRIPTOR.message_types_by_name['EtherbaseRequest']
_ETHERBASEREPLY = DESCRIPTOR.message_types_by_name['EtherbaseReply']
_NETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['NetVersionRequest']
_NETVERSIONREPLY = DESCRIPTOR.message_types_by_name['NetVersionReply']
_NETPEERCOUNTREQUEST = DESCRIPTOR.message_types_by_name['NetPeerCountRequest']
_NETPEERCOUNTREPLY = DESCRIPTOR.message_types_by_name['NetPeerCountReply']
_ENGINEGETPAYLOADREQUEST = DESCRIPTOR.message_types_by_name['EngineGetPayloadRequest']
_ENGINEPAYLOADSTATUS = DESCRIPTOR.message_types_by_name['EnginePayloadStatus']
_ENGINEPAYLOADATTRIBUTES = DESCRIPTOR.message_types_by_name['EnginePayloadAttributes']
_ENGINEFORKCHOICESTATE = DESCRIPTOR.message_types_by_name['EngineForkChoiceState']
_ENGINEFORKCHOICEUPDATEDREQUEST = DESCRIPTOR.message_types_by_name['EngineForkChoiceUpdatedRequest']
_ENGINEFORKCHOICEUPDATEDREPLY = DESCRIPTOR.message_types_by_name['EngineForkChoiceUpdatedReply']
_PROTOCOLVERSIONREQUEST = DESCRIPTOR.message_types_by_name['ProtocolVersionRequest']
_PROTOCOLVERSIONREPLY = DESCRIPTOR.message_types_by_name['ProtocolVersionReply']
_CLIENTVERSIONREQUEST = DESCRIPTOR.message_types_by_name['ClientVersionRequest']
_CLIENTVERSIONREPLY = DESCRIPTOR.message_types_by_name['ClientVersionReply']
_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRequest']
_SUBSCRIBEREPLY = DESCRIPTOR.message_types_by_name['SubscribeReply']
_LOGSFILTERREQUEST = DESCRIPTOR.message_types_by_name['LogsFilterRequest']
_SUBSCRIBELOGSREPLY = DESCRIPTOR.message_types_by_name['SubscribeLogsReply']
_BLOCKREQUEST = DESCRIPTOR.message_types_by_name['BlockRequest']
_BLOCKREPLY = DESCRIPTOR.message_types_by_name['BlockReply']
_TXNLOOKUPREQUEST = DESCRIPTOR.message_types_by_name['TxnLookupRequest']
_TXNLOOKUPREPLY = DESCRIPTOR.message_types_by_name['TxnLookupReply']
_NODESINFOREQUEST = DESCRIPTOR.message_types_by_name['NodesInfoRequest']
_NODESINFOREPLY = DESCRIPTOR.message_types_by_name['NodesInfoReply']
_PEERSREPLY = DESCRIPTOR.message_types_by_name['PeersReply']
_PENDINGBLOCKREPLY = DESCRIPTOR.message_types_by_name['PendingBlockReply']
EtherbaseRequest = _reflection.GeneratedProtocolMessageType('EtherbaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ETHERBASEREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EtherbaseRequest)
  })
_sym_db.RegisterMessage(EtherbaseRequest)

EtherbaseReply = _reflection.GeneratedProtocolMessageType('EtherbaseReply', (_message.Message,), {
  'DESCRIPTOR' : _ETHERBASEREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EtherbaseReply)
  })
_sym_db.RegisterMessage(EtherbaseReply)

NetVersionRequest = _reflection.GeneratedProtocolMessageType('NetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETVERSIONREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NetVersionRequest)
  })
_sym_db.RegisterMessage(NetVersionRequest)

NetVersionReply = _reflection.GeneratedProtocolMessageType('NetVersionReply', (_message.Message,), {
  'DESCRIPTOR' : _NETVERSIONREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NetVersionReply)
  })
_sym_db.RegisterMessage(NetVersionReply)

NetPeerCountRequest = _reflection.GeneratedProtocolMessageType('NetPeerCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETPEERCOUNTREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NetPeerCountRequest)
  })
_sym_db.RegisterMessage(NetPeerCountRequest)

NetPeerCountReply = _reflection.GeneratedProtocolMessageType('NetPeerCountReply', (_message.Message,), {
  'DESCRIPTOR' : _NETPEERCOUNTREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NetPeerCountReply)
  })
_sym_db.RegisterMessage(NetPeerCountReply)

EngineGetPayloadRequest = _reflection.GeneratedProtocolMessageType('EngineGetPayloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEGETPAYLOADREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EngineGetPayloadRequest)
  })
_sym_db.RegisterMessage(EngineGetPayloadRequest)

EnginePayloadStatus = _reflection.GeneratedProtocolMessageType('EnginePayloadStatus', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEPAYLOADSTATUS,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EnginePayloadStatus)
  })
_sym_db.RegisterMessage(EnginePayloadStatus)

EnginePayloadAttributes = _reflection.GeneratedProtocolMessageType('EnginePayloadAttributes', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEPAYLOADATTRIBUTES,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EnginePayloadAttributes)
  })
_sym_db.RegisterMessage(EnginePayloadAttributes)

EngineForkChoiceState = _reflection.GeneratedProtocolMessageType('EngineForkChoiceState', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEFORKCHOICESTATE,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EngineForkChoiceState)
  })
_sym_db.RegisterMessage(EngineForkChoiceState)

EngineForkChoiceUpdatedRequest = _reflection.GeneratedProtocolMessageType('EngineForkChoiceUpdatedRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEFORKCHOICEUPDATEDREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EngineForkChoiceUpdatedRequest)
  })
_sym_db.RegisterMessage(EngineForkChoiceUpdatedRequest)

EngineForkChoiceUpdatedReply = _reflection.GeneratedProtocolMessageType('EngineForkChoiceUpdatedReply', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEFORKCHOICEUPDATEDREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.EngineForkChoiceUpdatedReply)
  })
_sym_db.RegisterMessage(EngineForkChoiceUpdatedReply)

ProtocolVersionRequest = _reflection.GeneratedProtocolMessageType('ProtocolVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLVERSIONREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.ProtocolVersionRequest)
  })
_sym_db.RegisterMessage(ProtocolVersionRequest)

ProtocolVersionReply = _reflection.GeneratedProtocolMessageType('ProtocolVersionReply', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLVERSIONREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.ProtocolVersionReply)
  })
_sym_db.RegisterMessage(ProtocolVersionReply)

ClientVersionRequest = _reflection.GeneratedProtocolMessageType('ClientVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTVERSIONREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.ClientVersionRequest)
  })
_sym_db.RegisterMessage(ClientVersionRequest)

ClientVersionReply = _reflection.GeneratedProtocolMessageType('ClientVersionReply', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTVERSIONREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.ClientVersionReply)
  })
_sym_db.RegisterMessage(ClientVersionReply)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeReply = _reflection.GeneratedProtocolMessageType('SubscribeReply', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.SubscribeReply)
  })
_sym_db.RegisterMessage(SubscribeReply)

LogsFilterRequest = _reflection.GeneratedProtocolMessageType('LogsFilterRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGSFILTERREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.LogsFilterRequest)
  })
_sym_db.RegisterMessage(LogsFilterRequest)

SubscribeLogsReply = _reflection.GeneratedProtocolMessageType('SubscribeLogsReply', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBELOGSREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.SubscribeLogsReply)
  })
_sym_db.RegisterMessage(SubscribeLogsReply)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.BlockRequest)
  })
_sym_db.RegisterMessage(BlockRequest)

BlockReply = _reflection.GeneratedProtocolMessageType('BlockReply', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.BlockReply)
  })
_sym_db.RegisterMessage(BlockReply)

TxnLookupRequest = _reflection.GeneratedProtocolMessageType('TxnLookupRequest', (_message.Message,), {
  'DESCRIPTOR' : _TXNLOOKUPREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.TxnLookupRequest)
  })
_sym_db.RegisterMessage(TxnLookupRequest)

TxnLookupReply = _reflection.GeneratedProtocolMessageType('TxnLookupReply', (_message.Message,), {
  'DESCRIPTOR' : _TXNLOOKUPREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.TxnLookupReply)
  })
_sym_db.RegisterMessage(TxnLookupReply)

NodesInfoRequest = _reflection.GeneratedProtocolMessageType('NodesInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODESINFOREQUEST,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NodesInfoRequest)
  })
_sym_db.RegisterMessage(NodesInfoRequest)

NodesInfoReply = _reflection.GeneratedProtocolMessageType('NodesInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _NODESINFOREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.NodesInfoReply)
  })
_sym_db.RegisterMessage(NodesInfoReply)

PeersReply = _reflection.GeneratedProtocolMessageType('PeersReply', (_message.Message,), {
  'DESCRIPTOR' : _PEERSREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.PeersReply)
  })
_sym_db.RegisterMessage(PeersReply)

PendingBlockReply = _reflection.GeneratedProtocolMessageType('PendingBlockReply', (_message.Message,), {
  'DESCRIPTOR' : _PENDINGBLOCKREPLY,
  '__module__' : 'remote.ethbackend_pb2'
  # @@protoc_insertion_point(class_scope:remote.PendingBlockReply)
  })
_sym_db.RegisterMessage(PendingBlockReply)

_ETHBACKEND = DESCRIPTOR.services_by_name['ETHBACKEND']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017./remote;remote'
  _EVENT._serialized_start=1941
  _EVENT._serialized_end=2015
  _ENGINESTATUS._serialized_start=2017
  _ENGINESTATUS._serialized_end=2106
  _ETHERBASEREQUEST._serialized_start=83
  _ETHERBASEREQUEST._serialized_end=101
  _ETHERBASEREPLY._serialized_start=103
  _ETHERBASEREPLY._serialized_end=149
  _NETVERSIONREQUEST._serialized_start=151
  _NETVERSIONREQUEST._serialized_end=170
  _NETVERSIONREPLY._serialized_start=172
  _NETVERSIONREPLY._serialized_end=201
  _NETPEERCOUNTREQUEST._serialized_start=203
  _NETPEERCOUNTREQUEST._serialized_end=224
  _NETPEERCOUNTREPLY._serialized_start=226
  _NETPEERCOUNTREPLY._serialized_end=260
  _ENGINEGETPAYLOADREQUEST._serialized_start=262
  _ENGINEGETPAYLOADREQUEST._serialized_end=306
  _ENGINEPAYLOADSTATUS._serialized_start=308
  _ENGINEPAYLOADSTATUS._serialized_end=430
  _ENGINEPAYLOADATTRIBUTES._serialized_start=432
  _ENGINEPAYLOADATTRIBUTES._serialized_end=553
  _ENGINEFORKCHOICESTATE._serialized_start=556
  _ENGINEFORKCHOICESTATE._serialized_end=692
  _ENGINEFORKCHOICEUPDATEDREQUEST._serialized_start=695
  _ENGINEFORKCHOICEUPDATEDREQUEST._serialized_end=843
  _ENGINEFORKCHOICEUPDATEDREPLY._serialized_start=845
  _ENGINEFORKCHOICEUPDATEDREPLY._serialized_end=946
  _PROTOCOLVERSIONREQUEST._serialized_start=948
  _PROTOCOLVERSIONREQUEST._serialized_end=972
  _PROTOCOLVERSIONREPLY._serialized_start=974
  _PROTOCOLVERSIONREPLY._serialized_end=1008
  _CLIENTVERSIONREQUEST._serialized_start=1010
  _CLIENTVERSIONREQUEST._serialized_end=1032
  _CLIENTVERSIONREPLY._serialized_start=1034
  _CLIENTVERSIONREPLY._serialized_end=1072
  _SUBSCRIBEREQUEST._serialized_start=1074
  _SUBSCRIBEREQUEST._serialized_end=1121
  _SUBSCRIBEREPLY._serialized_start=1123
  _SUBSCRIBEREPLY._serialized_end=1182
  _LOGSFILTERREQUEST._serialized_start=1184
  _LOGSFILTERREQUEST._serialized_end=1305
  _SUBSCRIBELOGSREPLY._serialized_start=1308
  _SUBSCRIBELOGSREPLY._serialized_end=1553
  _BLOCKREQUEST._serialized_start=1555
  _BLOCKREQUEST._serialized_end=1622
  _BLOCKREPLY._serialized_start=1624
  _BLOCKREPLY._serialized_end=1671
  _TXNLOOKUPREQUEST._serialized_start=1673
  _TXNLOOKUPREQUEST._serialized_end=1721
  _TXNLOOKUPREPLY._serialized_start=1723
  _TXNLOOKUPREPLY._serialized_end=1760
  _NODESINFOREQUEST._serialized_start=1762
  _NODESINFOREQUEST._serialized_end=1795
  _NODESINFOREPLY._serialized_start=1797
  _NODESINFOREPLY._serialized_end=1854
  _PEERSREPLY._serialized_start=1856
  _PEERSREPLY._serialized_end=1900
  _PENDINGBLOCKREPLY._serialized_start=1902
  _PENDINGBLOCKREPLY._serialized_end=1939
  _ETHBACKEND._serialized_start=2109
  _ETHBACKEND._serialized_end=3234
# @@protoc_insertion_point(module_scope)
