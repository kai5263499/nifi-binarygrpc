# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import flowfile_service_pb2 as flowfile__service__pb2


class FlowFileServiceStub(object):
  """The FlowFile service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Send = channel.unary_unary(
        '/org.apache.nifi.processors.grpc.FlowFileService/Send',
        request_serializer=flowfile__service__pb2.FlowFileRequest.SerializeToString,
        response_deserializer=flowfile__service__pb2.FlowFileReply.FromString,
        )


class FlowFileServiceServicer(object):
  """The FlowFile service definition.
  """

  def Send(self, request, context):
    """Sends a FlowFile (blocking rpc)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FlowFileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Send': grpc.unary_unary_rpc_method_handler(
          servicer.Send,
          request_deserializer=flowfile__service__pb2.FlowFileRequest.FromString,
          response_serializer=flowfile__service__pb2.FlowFileReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.apache.nifi.processors.grpc.FlowFileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
