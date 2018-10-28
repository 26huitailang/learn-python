# coding: utf-8

"""
这个要求用linear time来解决，如果用heap维护窗口的话，每次移动都需要重新调整，最终复杂度是nlogk。
如果用队列(dequeue)来维护窗口，可以做到复杂度O(n)，总是保持窗口最左边是最大值，每个元素只需进入窗口一次，比较也是一次。
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        window, result = [], []  # window维护的是下标
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:  # 窗口有新元素，且第一个元素已经超过窗口
                window.pop(0)  # 弹出旧元素下标
            # 窗口的第一个元素小于新的，就弹出，直到最左边的是最大元素
            # 这里要从window右边出，因为如果最右边的元素都小于新元素的话，在新的窗口也没有意义
            while window and nums[window[-1]] <= x:
                window.pop()  # 弹出小的元素
            window.append(i)  # 小于k时
            print("window(下标): {}, result: {}".format(window, result))
            if i >= k - 1:  # 窗口填补超过k后，i是下标，所以k-1比较，每次淘汰完小的元素，结果就是窗口的第一个元素
                result.append(nums[window[0]])
        return result


def test():
    nums = [1, 3, 0, 5, 9, 0, 8, 7, 3, 0, 9]
    print(nums)
    solution = Solution()
    r = solution.maxSlidingWindow(nums, 3)
    print(r)


if __name__ == "__main__":
    test()
