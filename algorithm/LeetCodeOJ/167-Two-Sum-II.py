class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用字典来操作
        val_index_dict = dict()
        for i, v in enumerate(numbers):
            val_index_dict[v] = i
        
        for i in numbers:
            if (target - i) in val_index_dict:
                # 避免两个重复的值时只能定位到第一个
                # 从切片中定位再加切片的位置
                pos1 = numbers.index(i) 
                pos2 = val_index_dict[target - i]
                if pos1 < pos2:
                    return [pos1 + 1, pos2 + 1]
