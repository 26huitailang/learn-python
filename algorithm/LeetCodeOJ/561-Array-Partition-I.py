class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can't proof
        # 画图的话，比如4个数，总是0/2能得到最大的值
        # 复杂度依据排序的算法决定
        return sum([n for n in sorted(nums)[::2]])
