"""
这道题要求是不要额外的空间，时间复杂度是O(n)
我没有解出来，但是看其他人的答案，大概思路都是利用数组数字在长度区间的想法
也就是说，数组里面是一堆index + 1，要找重复出现过两次的index，方法是：
遍历数组，利用index去反转这个数字为负，如果再次检查到有负数，则表示index重复出现了，刚好是遍历一次数组
"""
import random


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1  # 反转为负数，再次检测到时，abs(x)重复
        return result


def main():
    length = 8
    nums = [random.randint(1, length) for x in range(length)]
    print(nums)
    s = Solution()
    result = s.findDuplicates(nums)
    print(result)

if __name__ == '__main__':
    main()
