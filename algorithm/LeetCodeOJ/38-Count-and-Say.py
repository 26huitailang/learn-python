"""
1.     1
2.     11
3.     21
4.     1211
5.     111221
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1' 
        while n - 1 > 0:  # loop for next word
            # init
            count = 0  # current count
            temp = ''  # next say
            char = result[0]  # counting character
            for c in result:  # loop for current word
                if c == char:  # same, plus 1
                    count += 1
                else:  # not same, update the say string
                    temp += str(count) + char
                    char = c  # change counting char
                    count = 1
            temp += str(count) + char
            result = temp  # next word
            n -= 1
        return result

