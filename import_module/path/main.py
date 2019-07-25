import os
import time


def success(**option):
    ret = {"status": True}

    ret.update(option)

    return ret


def fail(**option):
    ret = {"status": False}

    ret.update(option)

    return ret


def exploit():
    print("hello")
    os.makedirs("/tmp/{}".format(time.ctime()))
    return
