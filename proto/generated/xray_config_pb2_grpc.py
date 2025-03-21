# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import xray_config_pb2 as xray__config__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in xray_config_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class XrayConfigServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateClient = channel.unary_unary(
                '/xray_config.XrayConfigService/CreateClient',
                request_serializer=xray__config__pb2.CreateClientRequest.SerializeToString,
                response_deserializer=xray__config__pb2.OperationResponse.FromString,
                _registered_method=True)
        self.ReadClient = channel.unary_unary(
                '/xray_config.XrayConfigService/ReadClient',
                request_serializer=xray__config__pb2.ReadClientRequest.SerializeToString,
                response_deserializer=xray__config__pb2.Client.FromString,
                _registered_method=True)
        self.UpdateClient = channel.unary_unary(
                '/xray_config.XrayConfigService/UpdateClient',
                request_serializer=xray__config__pb2.UpdateClientRequest.SerializeToString,
                response_deserializer=xray__config__pb2.OperationResponse.FromString,
                _registered_method=True)
        self.DeleteClient = channel.unary_unary(
                '/xray_config.XrayConfigService/DeleteClient',
                request_serializer=xray__config__pb2.DeleteClientRequest.SerializeToString,
                response_deserializer=xray__config__pb2.OperationResponse.FromString,
                _registered_method=True)


class XrayConfigServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_XrayConfigServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateClient': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateClient,
                    request_deserializer=xray__config__pb2.CreateClientRequest.FromString,
                    response_serializer=xray__config__pb2.OperationResponse.SerializeToString,
            ),
            'ReadClient': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadClient,
                    request_deserializer=xray__config__pb2.ReadClientRequest.FromString,
                    response_serializer=xray__config__pb2.Client.SerializeToString,
            ),
            'UpdateClient': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateClient,
                    request_deserializer=xray__config__pb2.UpdateClientRequest.FromString,
                    response_serializer=xray__config__pb2.OperationResponse.SerializeToString,
            ),
            'DeleteClient': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteClient,
                    request_deserializer=xray__config__pb2.DeleteClientRequest.FromString,
                    response_serializer=xray__config__pb2.OperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xray_config.XrayConfigService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('xray_config.XrayConfigService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class XrayConfigService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/xray_config.XrayConfigService/CreateClient',
            xray__config__pb2.CreateClientRequest.SerializeToString,
            xray__config__pb2.OperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/xray_config.XrayConfigService/ReadClient',
            xray__config__pb2.ReadClientRequest.SerializeToString,
            xray__config__pb2.Client.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/xray_config.XrayConfigService/UpdateClient',
            xray__config__pb2.UpdateClientRequest.SerializeToString,
            xray__config__pb2.OperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/xray_config.XrayConfigService/DeleteClient',
            xray__config__pb2.DeleteClientRequest.SerializeToString,
            xray__config__pb2.OperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
