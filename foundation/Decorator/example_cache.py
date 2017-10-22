#!/usr/bin/python
# coding: UTF-8

import datetime
from functools import wraps

now = datetime.datetime.now


def cache(func):
    caches = {}

    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)
        return caches[args]

    return wrap


def fib(num):
    if num < 2:
        return 1
    return fib(num - 1) + fib(num - 2)


fib_with_cache = cache(fib)

start = now()
for i in range(10):
    fib(30)
end = now()
print("Fib without cache costs: %r" % (end - start))

start = now()
for _ in range(10):
    fib_with_cache(30)
end = now()
print("Fib with cache costs: %r" % (end - start))
