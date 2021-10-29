import grpc

from . import hello_pb2_grpc
from . import greeter_server


def serve():
    server = grpc.server()
    hello_pb2_grpc.add_GreeterServicer_to_server(greeter_server.Greeter(), server)
    server.add_insecure_port('[::]:8082')
    server.start()
    server.wait_for_termination()
