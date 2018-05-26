import grpc
from concurrent import futures
import time
import flowfile_service_pb2
import flowfile_service_pb2_grpc

class FlowFileServiceServer(flowfile_service_pb2_grpc.FlowFileServiceServicer):

    def Send(self, request, context):
        reply = flowfile_service_pb2.FlowFileReply()
        return reply

if __name__ == "__main__":
    print("alright alright alright")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    flowfile_service_pb2_grpc.add_FlowFileServiceServicer_to_server(
        FlowFileServiceServer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 9000.')
    server.add_insecure_port('[::]:9000')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)