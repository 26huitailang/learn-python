#!/usr/bin/env python
# coding: utf-8

"meTextFile.py -- create text file"

import os
ls = os.linesep  # 当前平台的终止符

# get filename
while True:
    fname = input('input filename: ')
    if os.path.exists(fname):
        print("ERROR: '%s' already exsits" % fname)
    else:
        break

# get file content lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates unput
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('Done!')
