#!/usr/bin/python
# coding: utf-8
import cProfile
from random import randint

def bubble(nList):
    for i in range(len(nList) - 1):
        for j in range(len(nList) - 1 - i):
            if nList[j] > nList[j + 1]:
                nList[j], nList[j + 1] = nList[j + 1], nList[j]
    print(nList)

if __name__ == '__main__':
    nums =[]
    for i in range(10000):
        nums.append(randint(1, 10000))
    cProfile.run('bubble(nums)')
