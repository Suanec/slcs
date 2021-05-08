# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/8.

class Solution(object):
    """
    498. Diagonal Traverse
    Medium

    1264

    415

    Add to List

    Share
    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.



    Example 1:


    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    Example 2:

    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]


    Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    -105 <= mat[i][j] <= 105
    """
    def findDiagonalOrder(self, mat):
        """
        Runtime: 180 ms, faster than 36.90% of Python online submissions for Diagonal Traverse.
        Memory Usage: 17.1 MB, less than 26.74% of Python online submissions for Diagonal Traverse.

        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rst_memo = {} # idx_sum : values righttop to leftbutton
        for row_idx in xrange(0, len(mat)):
            row = mat[row_idx]
            for col_idx in xrange(0, len(row)):
                elem = row[col_idx]
                idx_sum = row_idx + col_idx
                rst_stage = [elem] + rst_memo.get(idx_sum, []) if(0 == idx_sum % 2) else rst_memo.get(idx_sum, []) + [elem]
                rst_memo[idx_sum] = rst_stage
        rst = []
        for idx_sum in sorted(rst_memo.keys()):
            # rst += reversed(rst_memo[idx_sum])
            rst += rst_memo[idx_sum]
        return rst

    def self_testing(self):
        # [1,2,4,7,5,3,6,8,9]
        print(self.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
        # [1,2,3,4]
        print(self.findDiagonalOrder([[1,2],[3,4]]))

Solution().self_testing()
