#!/usr/bin/python
# coding: utf-8
from _functools import reduce
import pdb


def titleToNumber(s):
    pdb.set_trace()
    return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))


if __name__ == '__main__':
    titleToNumber('A')
