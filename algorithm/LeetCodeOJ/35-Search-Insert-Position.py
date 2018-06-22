class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = None
        for i in range(len(nums)):
            if nums[i] >= target:  # 大于等于都是返回当前位置
                return i
            else:  # 否则，位置是i+1
                pos = i + 1
        return pos