#!/usr/bin/python
# -*- coding: utf-8 -*-
#Fisher–Yates Shuffle
'''
 1. 从还没处理的数组（假如还剩k个）中，随机产生一个[0, k]之间的数字p（假设数组从0开始）；
 2. 从剩下的k个数中把第p个数取出；
 3. 重复步骤2和3直到数字全部取完；
 4. 从步骤3取出的数字序列便是一个打乱了的数列。
'''
import random

def shuffle1(lis):
  result = []
  while lis:
    p = random.randrange(0, len(lis))
    result.append(lis[p])
    lis.pop(p)
  return result

#Knuth-Durstenfeld Shuffle
def shuffle2(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
        print lis
    return lis
    
#Inside-Out Algorithm
def shuffle3(lis):
    result = lis[:]
    for i in range(1, len(lis)):
        j = random.randrange(0, i)
        result[i] = result[j]
        result[j] = lis[i]
        print result
    return result

# r = shuffle3([1, 2, 2, 3, 3, 4, 5, 10])