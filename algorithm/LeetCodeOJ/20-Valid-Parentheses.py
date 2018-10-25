class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # answer from discussion
        characters = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        stack = []
        for i in s:
            if i not in characters:
                # 将对应的后括号入栈
                stack.append(i)
            # 如果不是前括号，且也等于出栈的值，那么顺序不对
            # 这里是一个FILO
            elif not stack or characters[i] != stack.pop():
                return False
        return not stack


def main():
    sol = Solution()
    case1 = "{}[]()"
    assert sol.isValid(case1) is True
    case2 = "[[({})]]"
    assert sol.isValid(case2) is True
    case3 = "[]]"
    assert sol.isValid(case3) is False
    case4 = "[(])"
    assert sol.isValid(case4) is False


if __name__ == '__main__':
    main()
