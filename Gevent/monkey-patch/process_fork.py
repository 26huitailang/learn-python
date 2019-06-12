import gevent
from gevent import monkey
import socket
import time
from run_no_monkey_patch import no_patch
from multiprocessing import Process

monkey.patch_all()


def with_patch():
    fork = False
    while True:
        print("patch: {}".format(socket.socket))
        time.sleep(3)
        no_patch_process = Process(target=no_patch)
        no_patch_process.start()
        no_patch_process.join()


if __name__ == "__main__":
    with_patch()
