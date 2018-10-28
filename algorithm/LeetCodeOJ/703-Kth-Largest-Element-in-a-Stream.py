#!/usr/bin/env python
# coding=utf-8

"""
维护一个最大的k个值的容器，每次添加一个元素，返回最小的那个值。
如果用普通的数组，复杂度是nlogn，每个元素重新排序。
如果用min heap（最小堆，堆顶是最小元素），复杂度是logn，只需比较队顶元素，如果队顶小才重新调整堆的顺序，否则跳过
"""

import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # self.nums = nums
        self.k = k
        # heapq.heapify(self.nums)
        self.klargest = heapq.nlargest(k, nums)  # max heap
        heapq.heapify(self.klargest)  # change to min heap

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.klargest) < self.k:
            heapq.heappush(self.klargest, val)
            if len(self.klargest) == self.k:
                return self.klargest[0]
            else:
                return None
        elif self.klargest[0] < val:
            heapq.heappop(self.klargest)
            heapq.heappush(self.klargest, val)
        return self.klargest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def main():
    klargest = KthLargest(3, [4, 5, 8, 2])
    add_result_list = [(3, 4), (5, 5), (10, 5), (9, 8), (4, 8)]
    print("Inital: {}".format(klargest.klargest))
    for a, r in add_result_list:
        print(a, r)
        assert klargest.add(a) == r
        print(klargest.klargest)


if __name__ == '__main__':
    main()
