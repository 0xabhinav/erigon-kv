# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.txpool import txpool_pb2 as txpool_dot_txpool__pb2
from proto.types import types_pb2 as types_dot_types__pb2


class TxpoolStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Version = channel.unary_unary(
                '/txpool.Txpool/Version',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=types_dot_types__pb2.VersionReply.FromString,
                )
        self.FindUnknown = channel.unary_unary(
                '/txpool.Txpool/FindUnknown',
                request_serializer=txpool_dot_txpool__pb2.TxHashes.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.TxHashes.FromString,
                )
        self.Add = channel.unary_unary(
                '/txpool.Txpool/Add',
                request_serializer=txpool_dot_txpool__pb2.AddRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.AddReply.FromString,
                )
        self.Transactions = channel.unary_unary(
                '/txpool.Txpool/Transactions',
                request_serializer=txpool_dot_txpool__pb2.TransactionsRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.TransactionsReply.FromString,
                )
        self.All = channel.unary_unary(
                '/txpool.Txpool/All',
                request_serializer=txpool_dot_txpool__pb2.AllRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.AllReply.FromString,
                )
        self.Pending = channel.unary_unary(
                '/txpool.Txpool/Pending',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.PendingReply.FromString,
                )
        self.OnAdd = channel.unary_stream(
                '/txpool.Txpool/OnAdd',
                request_serializer=txpool_dot_txpool__pb2.OnAddRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.OnAddReply.FromString,
                )
        self.Status = channel.unary_unary(
                '/txpool.Txpool/Status',
                request_serializer=txpool_dot_txpool__pb2.StatusRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.StatusReply.FromString,
                )
        self.Nonce = channel.unary_unary(
                '/txpool.Txpool/Nonce',
                request_serializer=txpool_dot_txpool__pb2.NonceRequest.SerializeToString,
                response_deserializer=txpool_dot_txpool__pb2.NonceReply.FromString,
                )


class TxpoolServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Version(self, request, context):
        """Version returns the service version number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindUnknown(self, request, context):
        """preserves incoming order, changes amount, unknown hashes will be omitted
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Expecting signed transactions. Preserves incoming order and amount
        Adding txs as local (use P2P to add remote txs)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transactions(self, request, context):
        """preserves incoming order and amount, if some transaction doesn't exists in pool - returns nil in this slot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def All(self, request, context):
        """returns all transactions from tx pool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pending(self, request, context):
        """Returns all pending (processable) transactions, in ready-for-mining order
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnAdd(self, request, context):
        """subscribe to new transactions add event
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """returns high level status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Nonce(self, request, context):
        """returns nonce for given account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TxpoolServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=types_dot_types__pb2.VersionReply.SerializeToString,
            ),
            'FindUnknown': grpc.unary_unary_rpc_method_handler(
                    servicer.FindUnknown,
                    request_deserializer=txpool_dot_txpool__pb2.TxHashes.FromString,
                    response_serializer=txpool_dot_txpool__pb2.TxHashes.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=txpool_dot_txpool__pb2.AddRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.AddReply.SerializeToString,
            ),
            'Transactions': grpc.unary_unary_rpc_method_handler(
                    servicer.Transactions,
                    request_deserializer=txpool_dot_txpool__pb2.TransactionsRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.TransactionsReply.SerializeToString,
            ),
            'All': grpc.unary_unary_rpc_method_handler(
                    servicer.All,
                    request_deserializer=txpool_dot_txpool__pb2.AllRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.AllReply.SerializeToString,
            ),
            'Pending': grpc.unary_unary_rpc_method_handler(
                    servicer.Pending,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=txpool_dot_txpool__pb2.PendingReply.SerializeToString,
            ),
            'OnAdd': grpc.unary_stream_rpc_method_handler(
                    servicer.OnAdd,
                    request_deserializer=txpool_dot_txpool__pb2.OnAddRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.OnAddReply.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=txpool_dot_txpool__pb2.StatusRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.StatusReply.SerializeToString,
            ),
            'Nonce': grpc.unary_unary_rpc_method_handler(
                    servicer.Nonce,
                    request_deserializer=txpool_dot_txpool__pb2.NonceRequest.FromString,
                    response_serializer=txpool_dot_txpool__pb2.NonceReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'txpool.Txpool', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Txpool(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Version',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            types_dot_types__pb2.VersionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindUnknown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/FindUnknown',
            txpool_dot_txpool__pb2.TxHashes.SerializeToString,
            txpool_dot_txpool__pb2.TxHashes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Add',
            txpool_dot_txpool__pb2.AddRequest.SerializeToString,
            txpool_dot_txpool__pb2.AddReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Transactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Transactions',
            txpool_dot_txpool__pb2.TransactionsRequest.SerializeToString,
            txpool_dot_txpool__pb2.TransactionsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def All(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/All',
            txpool_dot_txpool__pb2.AllRequest.SerializeToString,
            txpool_dot_txpool__pb2.AllReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pending(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Pending',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            txpool_dot_txpool__pb2.PendingReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/txpool.Txpool/OnAdd',
            txpool_dot_txpool__pb2.OnAddRequest.SerializeToString,
            txpool_dot_txpool__pb2.OnAddReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Status',
            txpool_dot_txpool__pb2.StatusRequest.SerializeToString,
            txpool_dot_txpool__pb2.StatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Nonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/txpool.Txpool/Nonce',
            txpool_dot_txpool__pb2.NonceRequest.SerializeToString,
            txpool_dot_txpool__pb2.NonceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
