#!/usr/bin/env python
# coding=utf-8

"""
时间复杂度：O(n)，只需要遍历一次数组
空间复杂度：O(1)，直接交换位置的话，只需一个额外空间来实现
"""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 利用两个下标
        head = 0
        tail = len(A) - 1
        while head < tail:
            if A[head] % 2 == 0:
                if A[tail] % 2 == 0:  # 如果首尾都是偶数，head后移一位
                    head += 1
                else:  # head even, tail odd, correct
                    head += 1
                    tail -= 1
            else:  # head是奇数
                if A[tail] % 2 == 0:
                    A[head], A[tail] = A[tail], A[head]
                    head += 1
                    tail -= 1
                else:  # tail 奇数
                    tail -= 1
        return A


if __name__ == '__main__':
    case = [n for n in range(10)]
    print(case)
    s = Solution()
    a = s.sortArrayByParity(case)
    print(a)
