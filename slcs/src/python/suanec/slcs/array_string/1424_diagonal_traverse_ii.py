# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/8.

class Solution(object):
    """
    1424. Diagonal Traverse II
    Medium

    521

    63

    Add to List

    Share
    Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.


    Example 1:



    Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,4,2,7,5,3,8,6,9]
    Example 2:



    Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
    Example 3:

    Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
    Output: [1,4,2,5,3,8,6,9,7,10,11]
    Example 4:

    Input: nums = [[1,2,3,4,5,6]]
    Output: [1,2,3,4,5,6]


    Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i].length <= 10^5
    1 <= nums[i][j] <= 10^9
    There at most 10^5 elements in nums.

    """
    def findDiagonalOrder(self, nums):
        """
        Runtime: 1020 ms, faster than 25.76% of Python online submissions for Diagonal Traverse II.
        Memory Usage: 39.3 MB, less than 63.64% of Python online submissions for Diagonal Traverse II.

        without reverse
        Runtime: 908 ms, faster than 78.79% of Python online submissions for Diagonal Traverse II.
        Memory Usage: 39.5 MB, less than 63.64% of Python online submissions for Diagonal Traverse II.


        :type nums: List[List[int]]
        :rtype: List[int]
        """
        rst_memo = {} # idx_sum : values righttop to leftbutton
        for row_idx in xrange(0, len(nums)):
            row = nums[row_idx]
            for col_idx in xrange(0, len(row)):
                elem = row[col_idx]
                idx_sum = row_idx + col_idx
                rst_memo[idx_sum] = [elem] + rst_memo.get(idx_sum, [])
        rst = []
        for idx_sum in sorted(rst_memo.keys()):
            # rst += reversed(rst_memo[idx_sum])
            rst += rst_memo[idx_sum]
        return rst

    def self_testing(self):
        # [1,4,2,7,5,3,8,6,9]
        print(self.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
        # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        print(self.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
        # [1,4,2,5,3,8,6,9,7,10,11]
        print(self.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
        # [1,2,3,4,5,6]
        print(self.findDiagonalOrder([[1,2,3,4,5,6]]))

Solution().self_testing()
