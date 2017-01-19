#!/usr/bin/python
# coding: utf-8
from time import ctime,sleep

def music():
    for i in range(2):
        print "I was listening to music. %s" %ctime()
        sleep(1)

def move():
    for i in range(2):
        print "I was at the movies! %s" %ctime()
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print "all over %s" %ctime()
