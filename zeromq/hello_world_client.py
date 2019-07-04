import time
import zmq
from threading import Thread

def one_connection(name):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    for req in range(10):
        socket.send(b"Hello")
        message = socket.recv()
        print("p {}-{} Received reply [{}]".format(name, req, message))

def main():
    thread_num = 10
    for i in range(thread_num):
        t = Thread(target=one_connection, args=(i,))
        t.daemon = True
        t.start()
        t.join()

if __name__ == '__main__':
    main()
