#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#

import time
import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1, 100000)
    zipcode = 1000
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    msg = "%i %i %i" % (zipcode, temperature, relhumidity)
    time.sleep(1)
    socket.send_string(msg)
    print("Send", msg)
    time.sleep(1000)