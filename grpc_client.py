import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message

# expression = 'x+y+c'
# expression_and_value = {'x': 1, 'y': 2, 'c': 3}

expression = 111.123
number = calculator_pb2.Number(value = expression)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)