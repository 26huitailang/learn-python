#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by char
with open('test-bychar.txt', 'w') as af:
    with open('UnclassifiedLicense.txt', 'r') as f:
        while True:
            char = f.read(1)
            if not char:
                break
            lower = char.lower()
            af.write(lower)

# by line
with open('test-byline.txt', 'w') as af:
    with open('UnclassifiedLicense.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            upcase = line.upper()
            af.write(upcase)

# f = open(file)
# for char in f.read:
#     process(char)
# f.close()
#
# with open(file) as f:
#     for line in f.readlines():
#         process(line)
