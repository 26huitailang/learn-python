import gevent
from gevent import monkey
import socket
import time
from run_no_monkey_patch import no_patch

monkey.patch_all()


def with_patch():
    count = 0
    while True:
        print("patch: {}".format(socket.socket))
        time.sleep(3)
        count += 1
        if count >= 3:
            break


if __name__ == "__main__":
    with_patch()
    no_patch()
