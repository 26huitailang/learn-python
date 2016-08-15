#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'peter'

'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)
        # while b:
        #     x = a & b
        #     y = (a ^ b) << 1
        #     a = x, b = y
        # return a
