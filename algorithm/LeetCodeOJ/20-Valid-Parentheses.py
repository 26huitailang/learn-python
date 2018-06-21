class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # answer from discussion
        characters = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        cases = [""]  # 一个空字符串避免只有一个]这样符号的案例，不能pop
        for i in s:
            if i in characters:
                # 将对应的后括号入栈
                cases.append(characters[i])
            # 如果不是前括号，且也等于出栈的值，那么顺序不对
            # 这里是一个FILO
            elif i not in characters.keys() and i != cases.pop():
                return False

        return cases == [""]