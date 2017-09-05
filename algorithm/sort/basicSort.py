#!/usr/bin/python
# coding: utf-8
"""
几种基础排序算法的实现。

可以在/tests目录下进行测试对比，使用pytest。
"""


def bubble_sort(nums):
    """ 冒泡排序。

    :param nums: 待排序列表
    :return: 排序后的列表
    """
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def insert_sort(nums):
    """插入排序。

    :param nums: 待排序列表
    :return: 排序后的列表
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > key:
                nums[j + 1] = nums[j]
                nums[j] = key
            j -= 1

    return nums


def shell_sort():  # TODO
    pass


def quick_sort():  # TODO
    pass


def select_sort():  # TODO
    pass


def heap_sort():  # TODO
    pass


def merge_sort():  # TODO
    pass


def radix_sort():  # TODO
    pass


if __name__ == '__main__':
    nums = [12, 123, 34, 45, 767, 123, 2, 5, 7, 9, 123, 34345, 234134234]
    res = insert_sort(nums)
    print(res)