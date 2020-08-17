# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode-cn.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp_matrix = [
            [
                x for x in line
            ] for line in grid
        ]
        for row in xrange(0,len(dp_matrix)):
            for col in xrange(0,len(dp_matrix[row])):
                if(row < 1):
                    if(col > 0):
                        dp_matrix[row][col] = dp_matrix[row][col-1] + dp_matrix[row][col]
                else:
                    if(col == 0):
                        dp_matrix[row][col] = dp_matrix[row-1][col] + dp_matrix[row][col]
                    else:
                        left = dp_matrix[row][col-1] + dp_matrix[row][col]
                        up = dp_matrix[row-1][col] + dp_matrix[row][col]
                        dp_matrix[row][col] = min(left,up)
        return dp_matrix[row][col]
    def self_testing(self):
        test_grit = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]
        s = Solution()
        # print s.minPathSum(test_grit)
