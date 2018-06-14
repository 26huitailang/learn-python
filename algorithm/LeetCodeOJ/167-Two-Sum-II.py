class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers[i:]:
                # 避免两个重复的值时只能定位到第一个
                # 从切片中定位再加切片的位置
                return [i + 1, numbers[i:].index(target - numbers[i]) + 1 + i]

