class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        sum = 0
        i = len(s)
        while i > 0:
            # 先判断最后的两位有没有在组合里面，在的话左移两位
            if s[i-2:i] in table:
                sum += table[s[i-2:i]]
                i -= 2
            # 没有的话，计算一位，左移一位
            else:
                sum += table[s[i-1]]
                i -= 1

        return sum
