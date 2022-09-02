# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.p2psentry import sentry_pb2 as p2psentry_dot_sentry__pb2
from proto.types import types_pb2 as types_dot_types__pb2


class SentryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetStatus = channel.unary_unary(
                '/sentry.Sentry/SetStatus',
                request_serializer=p2psentry_dot_sentry__pb2.StatusData.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.SetStatusReply.FromString,
                )
        self.PenalizePeer = channel.unary_unary(
                '/sentry.Sentry/PenalizePeer',
                request_serializer=p2psentry_dot_sentry__pb2.PenalizePeerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.PeerMinBlock = channel.unary_unary(
                '/sentry.Sentry/PeerMinBlock',
                request_serializer=p2psentry_dot_sentry__pb2.PeerMinBlockRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandShake = channel.unary_unary(
                '/sentry.Sentry/HandShake',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.HandShakeReply.FromString,
                )
        self.SendMessageByMinBlock = channel.unary_unary(
                '/sentry.Sentry/SendMessageByMinBlock',
                request_serializer=p2psentry_dot_sentry__pb2.SendMessageByMinBlockRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.SentPeers.FromString,
                )
        self.SendMessageById = channel.unary_unary(
                '/sentry.Sentry/SendMessageById',
                request_serializer=p2psentry_dot_sentry__pb2.SendMessageByIdRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.SentPeers.FromString,
                )
        self.SendMessageToRandomPeers = channel.unary_unary(
                '/sentry.Sentry/SendMessageToRandomPeers',
                request_serializer=p2psentry_dot_sentry__pb2.SendMessageToRandomPeersRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.SentPeers.FromString,
                )
        self.SendMessageToAll = channel.unary_unary(
                '/sentry.Sentry/SendMessageToAll',
                request_serializer=p2psentry_dot_sentry__pb2.OutboundMessageData.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.SentPeers.FromString,
                )
        self.Messages = channel.unary_stream(
                '/sentry.Sentry/Messages',
                request_serializer=p2psentry_dot_sentry__pb2.MessagesRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.InboundMessage.FromString,
                )
        self.Peers = channel.unary_unary(
                '/sentry.Sentry/Peers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.PeersReply.FromString,
                )
        self.PeerCount = channel.unary_unary(
                '/sentry.Sentry/PeerCount',
                request_serializer=p2psentry_dot_sentry__pb2.PeerCountRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.PeerCountReply.FromString,
                )
        self.PeerById = channel.unary_unary(
                '/sentry.Sentry/PeerById',
                request_serializer=p2psentry_dot_sentry__pb2.PeerByIdRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.PeerByIdReply.FromString,
                )
        self.PeerEvents = channel.unary_stream(
                '/sentry.Sentry/PeerEvents',
                request_serializer=p2psentry_dot_sentry__pb2.PeerEventsRequest.SerializeToString,
                response_deserializer=p2psentry_dot_sentry__pb2.PeerEvent.FromString,
                )
        self.NodeInfo = channel.unary_unary(
                '/sentry.Sentry/NodeInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=types_dot_types__pb2.NodeInfoReply.FromString,
                )


class SentryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetStatus(self, request, context):
        """SetStatus - force new ETH client state of sentry - network_id, max_block, etc...
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PenalizePeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeerMinBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandShake(self, request, context):
        """HandShake - pre-requirement for all Send* methods - returns ETH protocol version,
        without knowledge of protocol - impossible encode correct P2P message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageByMinBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToRandomPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Messages(self, request, context):
        """Subscribe to receive messages.
        Calling multiple times with a different set of ids starts separate streams.
        It is possible to subscribe to the same set if ids more than once.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Peers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeerCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeerById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeerEvents(self, request, context):
        """Subscribe to notifications about connected or lost peers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NodeInfo(self, request, context):
        """NodeInfo returns a collection of metadata known about the host.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SentryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStatus,
                    request_deserializer=p2psentry_dot_sentry__pb2.StatusData.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.SetStatusReply.SerializeToString,
            ),
            'PenalizePeer': grpc.unary_unary_rpc_method_handler(
                    servicer.PenalizePeer,
                    request_deserializer=p2psentry_dot_sentry__pb2.PenalizePeerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'PeerMinBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.PeerMinBlock,
                    request_deserializer=p2psentry_dot_sentry__pb2.PeerMinBlockRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandShake': grpc.unary_unary_rpc_method_handler(
                    servicer.HandShake,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.HandShakeReply.SerializeToString,
            ),
            'SendMessageByMinBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageByMinBlock,
                    request_deserializer=p2psentry_dot_sentry__pb2.SendMessageByMinBlockRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.SentPeers.SerializeToString,
            ),
            'SendMessageById': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageById,
                    request_deserializer=p2psentry_dot_sentry__pb2.SendMessageByIdRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.SentPeers.SerializeToString,
            ),
            'SendMessageToRandomPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToRandomPeers,
                    request_deserializer=p2psentry_dot_sentry__pb2.SendMessageToRandomPeersRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.SentPeers.SerializeToString,
            ),
            'SendMessageToAll': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToAll,
                    request_deserializer=p2psentry_dot_sentry__pb2.OutboundMessageData.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.SentPeers.SerializeToString,
            ),
            'Messages': grpc.unary_stream_rpc_method_handler(
                    servicer.Messages,
                    request_deserializer=p2psentry_dot_sentry__pb2.MessagesRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.InboundMessage.SerializeToString,
            ),
            'Peers': grpc.unary_unary_rpc_method_handler(
                    servicer.Peers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.PeersReply.SerializeToString,
            ),
            'PeerCount': grpc.unary_unary_rpc_method_handler(
                    servicer.PeerCount,
                    request_deserializer=p2psentry_dot_sentry__pb2.PeerCountRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.PeerCountReply.SerializeToString,
            ),
            'PeerById': grpc.unary_unary_rpc_method_handler(
                    servicer.PeerById,
                    request_deserializer=p2psentry_dot_sentry__pb2.PeerByIdRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.PeerByIdReply.SerializeToString,
            ),
            'PeerEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.PeerEvents,
                    request_deserializer=p2psentry_dot_sentry__pb2.PeerEventsRequest.FromString,
                    response_serializer=p2psentry_dot_sentry__pb2.PeerEvent.SerializeToString,
            ),
            'NodeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.NodeInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=types_dot_types__pb2.NodeInfoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sentry.Sentry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sentry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/SetStatus',
            p2psentry_dot_sentry__pb2.StatusData.SerializeToString,
            p2psentry_dot_sentry__pb2.SetStatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PenalizePeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/PenalizePeer',
            p2psentry_dot_sentry__pb2.PenalizePeerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeerMinBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/PeerMinBlock',
            p2psentry_dot_sentry__pb2.PeerMinBlockRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandShake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/HandShake',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            p2psentry_dot_sentry__pb2.HandShakeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageByMinBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/SendMessageByMinBlock',
            p2psentry_dot_sentry__pb2.SendMessageByMinBlockRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.SentPeers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/SendMessageById',
            p2psentry_dot_sentry__pb2.SendMessageByIdRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.SentPeers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToRandomPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/SendMessageToRandomPeers',
            p2psentry_dot_sentry__pb2.SendMessageToRandomPeersRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.SentPeers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/SendMessageToAll',
            p2psentry_dot_sentry__pb2.OutboundMessageData.SerializeToString,
            p2psentry_dot_sentry__pb2.SentPeers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Messages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sentry.Sentry/Messages',
            p2psentry_dot_sentry__pb2.MessagesRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.InboundMessage.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/Peers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            p2psentry_dot_sentry__pb2.PeersReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeerCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/PeerCount',
            p2psentry_dot_sentry__pb2.PeerCountRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.PeerCountReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeerById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/PeerById',
            p2psentry_dot_sentry__pb2.PeerByIdRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.PeerByIdReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeerEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sentry.Sentry/PeerEvents',
            p2psentry_dot_sentry__pb2.PeerEventsRequest.SerializeToString,
            p2psentry_dot_sentry__pb2.PeerEvent.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sentry.Sentry/NodeInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            types_dot_types__pb2.NodeInfoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
