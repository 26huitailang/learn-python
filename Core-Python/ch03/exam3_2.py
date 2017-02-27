#!/usr/bin/env python
# coding: utf-8

"readTextFile.py -- read and display text file"

# get filename
fname = input('Enter filename: ')
print("")

# aatempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine.strip())
    fobj.close()