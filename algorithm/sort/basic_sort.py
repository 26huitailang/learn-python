#!/usr/bin/python
# coding: utf-8
"""
几种基础排序算法的实现。

可以在/tests目录下进行测试对比，使用pytest。
"""
import random
import math


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


def insert_sort(arr):
    """ 插入排序。现实中的摸牌排序操作。

    :param arr: 待排序列表
    :return: 排序后的列表
    """
    # 从两个数据开始，每次添加一位，直到覆盖整组数据
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 每次与前一位比较，直到新的数据插入完成
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1

    return arr


def shell_sort(arr):
    """ 希尔排序。
    
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
                arr[j - step] = temp
                j -= step
        step //= 3

    return arr


def shell_sort_two(arr):
    """ 希尔排序，gap每次取一半，速度会比第一种方式快接近一倍。

    :param arr:
    :return:
    """
    count = len(arr)
    step = 2  # 每次减小增量为上一个的一半
    gap = count // step  # 增量
    while gap > 0:
        for i in range(0, gap):
            j = i + gap  # 离 i 位置gap距离的元素
            while j < count:
                # 向前比较
                k = j - gap
                temp = arr[j]
                # 如果前面的数大则交换位置，k继续向前，其实就是插入排序
                while k >= 0 and arr[k] > arr[j]:
                    arr[j] = arr[k]
                    arr[k] = temp
                    k -= gap
                # j往后探索，加入一个新的元素
                j += gap
        # 减小增量
        gap //= step

    return arr


def quick_sort(arr, low, high):
    """ 快速排序，数据量大的时候比希尔快一倍左右。

    :param arr: 待排序数据
    :param low: 低位
    :param high: 高位
    :return: 排序完成的数据
    """
    i = low  # 最低位标志
    j = high  # 最高位标志
    # 探索位置重叠
    if i >= j:
        return arr
    key = arr[i]  # 确定key值，大的放右边，小的放左边
    while i < j:
        while i < j and arr[j] >= key:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= key:
            i += 1
        arr[j] = arr[i]
    # 完成一次比较后再将key值赋值
    arr[i] = key
    # 继续将上次key值的结果递归
    quick_sort(arr, low, i - 1)
    quick_sort(arr, j + 1, high)
    return arr


def select_sort(arr):
    """ 直接选择排序。

    :param arr: 待排序数据
    :return: 已排序数据
    """
    count = len(arr)
    for i in range(0, count):
        low = i  # 记录第一个为最小值
        for j in range(i + 1, count):
            if arr[low] > arr[j]:
                low = j  # 每次只记录比较最小值的位置
        arr[low], arr[i] = arr[i], arr[low]  # 最小值放到当前列表的最前面

    return arr


def max_heapify(arr, root, size):
    """ 维护堆，使得子节点小于父节点。

    :param arr: 待排序列表
    :param root: 根节点
    :param size: 列表大小
    :return: None
    """
    lchild = 2 * root + 1
    rchild = 2 * root + 2
    largest = root
    if root < size // 2:
        if lchild < size and arr[lchild] > arr[largest]:
            largest = lchild
        if rchild < size and arr[rchild] > arr[largest]:
            largest = rchild
        if largest != root:
            arr[largest], arr[root] = arr[root], arr[largest]
            max_heapify(arr, largest, size)


def build_max_heap(arr, size):
    """ 构建最大堆。

    :param arr: 待排序数据
    :return: None
    """
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(arr, i, size)


def heap_sort(arr):
    """ 堆排序。

    :param arr: 待排序数据
    :return: None
    """
    size = len(arr)
    build_max_heap(arr, size)
    for i in range(size - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)


def merge(left, right):
    """ 合并。

    :param left: 左半序列
    :param right: 右半序列
    :return: 合并排序结果
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 当一边取完的时候，合并剩下的部分
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr):
    """ 归并排序。

    :param arr: 待排序数据
    :return: 合并结果
    """
    if len(arr) <= 1:
        return arr
    q = len(arr) // 2
    # 递归分解
    left = merge_sort(arr[:q])
    right = merge_sort(arr[q:])
    return merge(left, right)


def radix_sort(arr, radix=10):
    """ 基数排序。属于分配式排序distribution sort，又称桶子法bucket sort。

    :param arr: 待排序数据
    :param radix: 桶的数量，默认10个
    :return: 已排序数据
    """
    # 确定最大数的位数，决定排序趟数，ceil返回天花板值的float型
    k = int(math.ceil(math.log(max(arr), 10)))
    for i in range(k):
        # 生成radix个桶，每次位循环完成清空buckets
        buckets = [[] for i in range(radix)]
        for j in arr:
            buckets[j // radix ** i % radix].append(j)
        arr = [num for bucket in buckets for num in bucket]

    return arr


if __name__ == '__main__':
    arr = [i for i in range(20)]
    random.shuffle(arr)
    arr_b = arr.copy()
    res = radix_sort(arr_b)
    print(res)
