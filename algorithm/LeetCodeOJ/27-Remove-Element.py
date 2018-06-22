class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 遇到不一样的元素放到最初的位置，+1探索下一个不一致的元素
        length = 0
        for num in nums:
            if num != val:
                nums[length] = num
                length += 1
        
        return length