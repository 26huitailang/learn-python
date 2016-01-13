# -*- coding:utf-8 -*-
import os
dir="D:\\module"
data = []
for root,dirs,files in os.walk(dir):
    for file in dirs:
        print os.path.join(root,file)
# print data