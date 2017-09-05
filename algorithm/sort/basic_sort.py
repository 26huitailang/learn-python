#!/usr/bin/python
# coding: utf-8
"""
几种基础排序算法的实现。

可以在/tests目录下进行测试对比，使用pytest。
"""


def bubble_sort(arr):
    """ 冒泡排序。

    :param arr: 待排序列表
    :return: 排序后的列表
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insert_sort(arr):
    """插入排序。

    :param arr: 待排序列表
    :return: 排序后的列表
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1

    return arr


def shell_sort(arr):
    """希尔排序。
    
    :param arr: 待排序列表
    :return: 排序后的列表
    """
    count = len(arr)
    step = 1
    while step < count // 3:
        step = 3 * step + 1
    while step >= 1:
        for i in range(step, count):
            j = i
            temp = arr[j]
            while j >= step and arr[j] < arr[j - step]:
                arr[j] = arr[j - step]
                arr[j-step] = temp
                j -= step
        step = step // 3

    return arr


def shell_sort_two(arr):
    """希尔排序，gap每次取一半，速度会比第一种方式快接近一倍。

    :param arr:
    :return:
    """
    count = len(arr)
    step = 2
    gap = count // step
    while gap > 0:
        for i in range(0, gap):
            j = i + gap
            while j < count:
                k = j - gap
                temp = arr[j]
                while k >= 0 and arr[k] > arr[j]:
                    arr[j] = arr[k]
                    arr[k] = temp
                    k -= gap
                j += gap
        gap = gap // step

    return arr


def quick_sort(arr, low, high):
    """快速排序，数据量大的时候比希尔快一倍左右。

    :param arr: 待排序数据
    :param low: 低位
    :param high: 高位
    :return: 排序完成的数据
    """
    i = low
    j = high
    if i >= j:
        return arr
    key = arr[i]
    while i < j:
        while i < j and arr[j] >= key:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= key:
            i += 1
        arr[j] = arr[i]
    arr[i] = key
    quick_sort(arr, low, i - 1)
    quick_sort(arr, j + 1, high)
    return arr


def select_sort():  # TODO
    pass


def heap_sort():  # TODO
    pass


def merge_sort():  # TODO
    pass


def radix_sort():  # TODO
    # TODO 完成所有算法后，可图形化展示不同量级的速度比较，matplotlib画图
    pass


if __name__ == '__main__':
    arr = [12, 123, 34, 45, 767, 2, 5, 7, 9, 123, 34345, 234134234]
    arr_b = arr.copy()
    res = quick_sort(arr_b, 0, len(arr_b) - 1)
    print(res)
