#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        for i in range(n):
            matrix[i].reverse()

# Testcase
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]