#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.connect("tcp://localhost:5560")

while True:
    # message = socket.recv()
    message = socket.recv_multipart()
    print("Received request: %s" % message)
    socket.send(b"World")
