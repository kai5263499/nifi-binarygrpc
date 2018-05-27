import grpc
from concurrent import futures
import time
import flowfile_service_pb2
import flowfile_service_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:9001')
  stub = flowfile_service_pb2_grpc.FlowFileServiceStub(channel)
  request = flowfile_service_pb2.FlowFileRequest(id=1, attributes={'myattribute':'the value'})
  reply = stub.Send(request)
  print(reply)

if __name__ == '__main__':
  run()