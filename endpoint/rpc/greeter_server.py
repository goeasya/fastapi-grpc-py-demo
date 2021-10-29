import grpc
from . import hello_pb2
from . import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    def say_hello(self, request, context):
        return hello_pb2.HelloReply(message="hello.")



