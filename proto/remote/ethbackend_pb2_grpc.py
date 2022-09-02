# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.remote import ethbackend_pb2 as remote_dot_ethbackend__pb2
from proto.types import types_pb2 as types_dot_types__pb2


class ETHBACKENDStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Etherbase = channel.unary_unary(
                '/remote.ETHBACKEND/Etherbase',
                request_serializer=remote_dot_ethbackend__pb2.EtherbaseRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.EtherbaseReply.FromString,
                )
        self.NetVersion = channel.unary_unary(
                '/remote.ETHBACKEND/NetVersion',
                request_serializer=remote_dot_ethbackend__pb2.NetVersionRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.NetVersionReply.FromString,
                )
        self.NetPeerCount = channel.unary_unary(
                '/remote.ETHBACKEND/NetPeerCount',
                request_serializer=remote_dot_ethbackend__pb2.NetPeerCountRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.NetPeerCountReply.FromString,
                )
        self.EngineGetPayloadV1 = channel.unary_unary(
                '/remote.ETHBACKEND/EngineGetPayloadV1',
                request_serializer=remote_dot_ethbackend__pb2.EngineGetPayloadRequest.SerializeToString,
                response_deserializer=types_dot_types__pb2.ExecutionPayload.FromString,
                )
        self.EngineNewPayloadV1 = channel.unary_unary(
                '/remote.ETHBACKEND/EngineNewPayloadV1',
                request_serializer=types_dot_types__pb2.ExecutionPayload.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.EnginePayloadStatus.FromString,
                )
        self.EngineForkChoiceUpdatedV1 = channel.unary_unary(
                '/remote.ETHBACKEND/EngineForkChoiceUpdatedV1',
                request_serializer=remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedReply.FromString,
                )
        self.Version = channel.unary_unary(
                '/remote.ETHBACKEND/Version',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=types_dot_types__pb2.VersionReply.FromString,
                )
        self.ProtocolVersion = channel.unary_unary(
                '/remote.ETHBACKEND/ProtocolVersion',
                request_serializer=remote_dot_ethbackend__pb2.ProtocolVersionRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.ProtocolVersionReply.FromString,
                )
        self.ClientVersion = channel.unary_unary(
                '/remote.ETHBACKEND/ClientVersion',
                request_serializer=remote_dot_ethbackend__pb2.ClientVersionRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.ClientVersionReply.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/remote.ETHBACKEND/Subscribe',
                request_serializer=remote_dot_ethbackend__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.SubscribeReply.FromString,
                )
        self.SubscribeLogs = channel.stream_stream(
                '/remote.ETHBACKEND/SubscribeLogs',
                request_serializer=remote_dot_ethbackend__pb2.LogsFilterRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.SubscribeLogsReply.FromString,
                )
        self.Block = channel.unary_unary(
                '/remote.ETHBACKEND/Block',
                request_serializer=remote_dot_ethbackend__pb2.BlockRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.BlockReply.FromString,
                )
        self.TxnLookup = channel.unary_unary(
                '/remote.ETHBACKEND/TxnLookup',
                request_serializer=remote_dot_ethbackend__pb2.TxnLookupRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.TxnLookupReply.FromString,
                )
        self.NodeInfo = channel.unary_unary(
                '/remote.ETHBACKEND/NodeInfo',
                request_serializer=remote_dot_ethbackend__pb2.NodesInfoRequest.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.NodesInfoReply.FromString,
                )
        self.Peers = channel.unary_unary(
                '/remote.ETHBACKEND/Peers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.PeersReply.FromString,
                )
        self.PendingBlock = channel.unary_unary(
                '/remote.ETHBACKEND/PendingBlock',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=remote_dot_ethbackend__pb2.PendingBlockReply.FromString,
                )


class ETHBACKENDServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Etherbase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NetVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NetPeerCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EngineGetPayloadV1(self, request, context):
        """------------------------------------------------------------------------
        "The Merge" RPC requests natively implemented in the Erigon node backend

        Fetch Execution Payload using its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EngineNewPayloadV1(self, request, context):
        """Validate and possibly execute the payload.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EngineForkChoiceUpdatedV1(self, request, context):
        """Update fork choice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Version(self, request, context):
        """End of the Merge requests
        ------------------------------------------------------------------------

        Version returns the service version number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProtocolVersion(self, request, context):
        """ProtocolVersion returns the Ethereum protocol version number (e.g. 66 for ETH66).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientVersion(self, request, context):
        """ClientVersion returns the Ethereum client version string using node name convention (e.g. TurboGeth/v2021.03.2-alpha/Linux).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeLogs(self, request_iterator, context):
        """Only one subscription is needed to serve all the users, LogsFilterRequest allows to dynamically modifying the subscription
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Block(self, request, context):
        """High-level method - can read block from db, snapshots or apply any other logic
        it doesn't provide consistency
        Request fields are optional - it's ok to request block only by hash or only by number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TxnLookup(self, request, context):
        """High-level method - can find block number by txn hash
        it doesn't provide consistency
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NodeInfo(self, request, context):
        """NodeInfo collects and returns NodeInfo from all running sentry instances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Peers(self, request, context):
        """Peers collects and returns peers information from all running sentry instances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PendingBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ETHBACKENDServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Etherbase': grpc.unary_unary_rpc_method_handler(
                    servicer.Etherbase,
                    request_deserializer=remote_dot_ethbackend__pb2.EtherbaseRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.EtherbaseReply.SerializeToString,
            ),
            'NetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.NetVersion,
                    request_deserializer=remote_dot_ethbackend__pb2.NetVersionRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.NetVersionReply.SerializeToString,
            ),
            'NetPeerCount': grpc.unary_unary_rpc_method_handler(
                    servicer.NetPeerCount,
                    request_deserializer=remote_dot_ethbackend__pb2.NetPeerCountRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.NetPeerCountReply.SerializeToString,
            ),
            'EngineGetPayloadV1': grpc.unary_unary_rpc_method_handler(
                    servicer.EngineGetPayloadV1,
                    request_deserializer=remote_dot_ethbackend__pb2.EngineGetPayloadRequest.FromString,
                    response_serializer=types_dot_types__pb2.ExecutionPayload.SerializeToString,
            ),
            'EngineNewPayloadV1': grpc.unary_unary_rpc_method_handler(
                    servicer.EngineNewPayloadV1,
                    request_deserializer=types_dot_types__pb2.ExecutionPayload.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.EnginePayloadStatus.SerializeToString,
            ),
            'EngineForkChoiceUpdatedV1': grpc.unary_unary_rpc_method_handler(
                    servicer.EngineForkChoiceUpdatedV1,
                    request_deserializer=remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedReply.SerializeToString,
            ),
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=types_dot_types__pb2.VersionReply.SerializeToString,
            ),
            'ProtocolVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ProtocolVersion,
                    request_deserializer=remote_dot_ethbackend__pb2.ProtocolVersionRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.ProtocolVersionReply.SerializeToString,
            ),
            'ClientVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientVersion,
                    request_deserializer=remote_dot_ethbackend__pb2.ClientVersionRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.ClientVersionReply.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=remote_dot_ethbackend__pb2.SubscribeRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.SubscribeReply.SerializeToString,
            ),
            'SubscribeLogs': grpc.stream_stream_rpc_method_handler(
                    servicer.SubscribeLogs,
                    request_deserializer=remote_dot_ethbackend__pb2.LogsFilterRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.SubscribeLogsReply.SerializeToString,
            ),
            'Block': grpc.unary_unary_rpc_method_handler(
                    servicer.Block,
                    request_deserializer=remote_dot_ethbackend__pb2.BlockRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.BlockReply.SerializeToString,
            ),
            'TxnLookup': grpc.unary_unary_rpc_method_handler(
                    servicer.TxnLookup,
                    request_deserializer=remote_dot_ethbackend__pb2.TxnLookupRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.TxnLookupReply.SerializeToString,
            ),
            'NodeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.NodeInfo,
                    request_deserializer=remote_dot_ethbackend__pb2.NodesInfoRequest.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.NodesInfoReply.SerializeToString,
            ),
            'Peers': grpc.unary_unary_rpc_method_handler(
                    servicer.Peers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.PeersReply.SerializeToString,
            ),
            'PendingBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.PendingBlock,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=remote_dot_ethbackend__pb2.PendingBlockReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'remote.ETHBACKEND', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ETHBACKEND(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Etherbase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/Etherbase',
            remote_dot_ethbackend__pb2.EtherbaseRequest.SerializeToString,
            remote_dot_ethbackend__pb2.EtherbaseReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/NetVersion',
            remote_dot_ethbackend__pb2.NetVersionRequest.SerializeToString,
            remote_dot_ethbackend__pb2.NetVersionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NetPeerCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/NetPeerCount',
            remote_dot_ethbackend__pb2.NetPeerCountRequest.SerializeToString,
            remote_dot_ethbackend__pb2.NetPeerCountReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EngineGetPayloadV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/EngineGetPayloadV1',
            remote_dot_ethbackend__pb2.EngineGetPayloadRequest.SerializeToString,
            types_dot_types__pb2.ExecutionPayload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EngineNewPayloadV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/EngineNewPayloadV1',
            types_dot_types__pb2.ExecutionPayload.SerializeToString,
            remote_dot_ethbackend__pb2.EnginePayloadStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EngineForkChoiceUpdatedV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/EngineForkChoiceUpdatedV1',
            remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedRequest.SerializeToString,
            remote_dot_ethbackend__pb2.EngineForkChoiceUpdatedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/Version',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            types_dot_types__pb2.VersionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProtocolVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/ProtocolVersion',
            remote_dot_ethbackend__pb2.ProtocolVersionRequest.SerializeToString,
            remote_dot_ethbackend__pb2.ProtocolVersionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/ClientVersion',
            remote_dot_ethbackend__pb2.ClientVersionRequest.SerializeToString,
            remote_dot_ethbackend__pb2.ClientVersionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/remote.ETHBACKEND/Subscribe',
            remote_dot_ethbackend__pb2.SubscribeRequest.SerializeToString,
            remote_dot_ethbackend__pb2.SubscribeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeLogs(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/remote.ETHBACKEND/SubscribeLogs',
            remote_dot_ethbackend__pb2.LogsFilterRequest.SerializeToString,
            remote_dot_ethbackend__pb2.SubscribeLogsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Block(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/Block',
            remote_dot_ethbackend__pb2.BlockRequest.SerializeToString,
            remote_dot_ethbackend__pb2.BlockReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TxnLookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/TxnLookup',
            remote_dot_ethbackend__pb2.TxnLookupRequest.SerializeToString,
            remote_dot_ethbackend__pb2.TxnLookupReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NodeInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/NodeInfo',
            remote_dot_ethbackend__pb2.NodesInfoRequest.SerializeToString,
            remote_dot_ethbackend__pb2.NodesInfoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Peers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/Peers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            remote_dot_ethbackend__pb2.PeersReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PendingBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.ETHBACKEND/PendingBlock',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            remote_dot_ethbackend__pb2.PendingBlockReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
