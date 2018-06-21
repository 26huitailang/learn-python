class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if not strs:
            return result
        # 将字符串改为索引字典的格式，判断每一位上是否一致
        d_list = [{i: j for i,j in enumerate(x)} for x in strs]
        for i in range(len(strs[0])):
            c = ""  # 默认为空
            for j in range(len(d_list)):  # 遍历每个字符
                if i not in d_list[j]:  # 如果索引不在表示超过了最短字符
                    return result
                if not c:  # 如果c为空，表示第一次，那么赋值为要比对的字符
                    c = d_list[j][i]
                else:
                    if d_list[j][i] != c:  # 如果同位置不相同，则标志终止，返回结果
                        return result
                    
            result += c
        return result