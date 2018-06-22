class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用一个中间变量，遇到不相同的+1，换掉这个字符
        if not nums:
            return 0
        c = nums[0] - 1  # 比第一个元素小，这样可以从头到位比对
        length = 0
        for num in nums:  # 遇到后面与前面不相等的元素就将该元素放到量取的length位置
            if c != num:
                nums[length] = num  # 将不一致的元素放到这个位置
                length += 1  # 位置向前移动
                c = num
        
        return length
        
        
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    s.removeDuplicates(nums) == 5