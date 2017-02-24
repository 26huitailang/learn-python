# coding: utf-8
import time


def profile(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print '{} COST: {}'.format(func.__name__, end - start)
    return wrapper

COUNTS = 100000
@profile
def jiexi():
    l = [n ** 2 for n in range(COUNTS)]

@profile
def xunhuan():
    l = []
    for i in range(COUNTS):
        l.append(i ** 2)

jiexi()
xunhuan()