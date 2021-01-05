# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.cost_saving.v1 import statistic_pb2 as spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2


class StatisticStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/spaceone.api.cost_saving.v1.Statistic/list',
                request_serializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticsInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.cost_saving.v1.Statistic/stat',
                request_serializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class StatisticServicer(object):
    """Missing associated documentation comment in .proto file."""

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatisticServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_saving.v1.Statistic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Statistic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_saving.v1.Statistic/list',
            spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticQuery.SerializeToString,
            spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.cost_saving.v1.Statistic/stat',
            spaceone_dot_api_dot_cost__saving_dot_v1_dot_statistic__pb2.StatisticStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
