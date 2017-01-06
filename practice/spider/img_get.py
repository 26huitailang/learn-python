# coding: utf-8

import requests
import re

file = u'd:\OneDrive\文档\image.txt'
pattern = re.compile(r'https?://i\.imgur\.com/(\w+)\.(\w+)')
with open(file) as f:
    for line in f.readlines():
        items = re.findall(pattern, line)
        name = items[0][0]
        # print name
        fmt = items[0][1]
        print name, fmt
        img = requests.get(line)
        imgfile = open('d:\mzitu\\' + name + '.' + fmt, 'ab')
        imgfile.write(img.content)
        imgfile.close()
