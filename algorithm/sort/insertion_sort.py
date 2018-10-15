#!/usr/bin/env python
# coding=utf-8

import random

def insertion_sort(arr):
    if len(arr) <= 1:
        return
    for i in range(1, len(arr)):  # 从第二个元素开始，与前面的比较
        val = arr[i]
        j = i - 1
        while j >= 0:  # i 之前的元素
            if arr[j] > val:
                arr[j + 1] = arr[j]  # 往后移动
                j -= 1
            else:
                break
        arr[j + 1] = val  # 插入到比它小或相等位置后面


def main():
    arr = [random.randint(0, 1000) for i in range(0, 1000)]
    insertion_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
