#!/usr/bin/env python
# coding=utf-8

"""
原地排序：O(1)
时间复杂度：O(n^2)

经过测试，在可接受的执行时间内，优化不明显
"""

import random
import time


def bubble_sort(arr):
    """ 冒泡排序。

    :param arr: 待排序列表
    :return: 排序后的列表
    """
    # 每次循环留下 i 位置的最小值，值大的会向上冒泡
    for i in range(len(arr) - 1):
        # i 值往后的遍历
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def optimized_bubble_sort(arr):
    """ 优化的冒泡排序，如果没有发生交换，认为交换终止
    """
    for i in range(len(arr) - 1):
        flag = False
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
        if not flag:
            break

    return arr


def main():
    count = 2000
    arr = [random.randint(0, 1000) for _ in range(count)]
    tmp = arr.copy()
    start = time.time()
    result = bubble_sort(arr)
    print(time.time() - start)
    # print(result)
    start = time.time()
    result_2 = optimized_bubble_sort(tmp)
    print(time.time() - start)
    # print(result_2)


if __name__ == '__main__':
    main()
