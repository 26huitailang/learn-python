# coding: utf-8
"""
不是尾递归实现，会超过python的最大深度，在1000左右
python不提供尾递归，但是可以用生成器模拟尾递归的实现
或者用循环来替换，循环相比递归只是可读性不太好
"""

def factorial(n):
    # 0! = 1! = 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    factorial(5)
