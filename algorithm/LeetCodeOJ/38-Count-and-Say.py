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
        if n == 1:
            return n

        while n - 1 > 0:
            counter = 0


