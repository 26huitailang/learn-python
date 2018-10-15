#!/usr/bin/python
# coding: utf-8

"""
利用单元测试的结果 > logs.json作图比较不同排序算法的曲线
"""

import numpy as np
import matplotlib.pyplot as plt
import json

f = open('logs.json')
data = json.load(f)
print(data)

lens = []
funcs = []
for key, value in data.items():
    lens.append(int(key))
    for k, v in value.items():
        if k not in funcs:
            funcs.append(k)

# 重新分类数据
y = {}
for key in funcs:
    y[key] = {}
    for i in lens:
        y[key][i] = data[str(i)][key]
print(y)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(8, 4))
plt.xlabel("Data length")
plt.ylabel("Time(s)")
plt.title("各个排序算法时间比较")
for k, v in y.items():
    x = lens
    y = [value for key, value in v.items()]
    plt.plot(x, y, label="%s" % k, marker='*')
plt.legend()
plt.show()
