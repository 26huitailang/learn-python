# coding: utf-8

"""
时间复杂度 O(n), n 是A中所有元素的个数
空间复杂度 O(1)
"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 这个写法是为了分析复杂度
        # reverse rows
        for i in range(len(A)):
            head = 0
            tail = len(A) - 1
            while head < tail:
                A[i][head], A[i][tail] = A[i][tail], A[i][head]
                head += 1
                tail -= 1
            for j, val in enumerate(A[i]):
                A[i][j] = 1 ^ val
        
        # one-line version in discuss
        # invert first then reverse row
        # return [1 ^ i for i in row[::-1] for row in A[::-1]]
        return A


def main():
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(A)
    s = Solution()
    A = s.flipAndInvertImage(A)
    print(A)

if __name__ == '__main__':
    main()
