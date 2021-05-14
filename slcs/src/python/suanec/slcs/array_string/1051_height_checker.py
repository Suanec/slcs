# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/14. 

class Solution(object):
    """

    1051. Height Checker
    Easy

    54

    10

    Add to List

    Share
    A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].



    Example 1:

    Input: heights = [1,1,4,2,1,3]
    Output: 3
    Explanation:
    heights:  [1,1,4,2,1,3]
    expected: [1,1,1,2,3,4]
    Indices 2, 4, and 5 do not match.
    Example 2:

    Input: heights = [5,1,2,3,4]
    Output: 5
    Explanation:
    heights:  [5,1,2,3,4]
    expected: [1,2,3,4,5]
    All indices do not match.
    Example 3:

    Input: heights = [1,2,3,4,5]
    Output: 0
    Explanation:
    heights:  [1,2,3,4,5]
    expected: [1,2,3,4,5]
    All indices match.


    Constraints:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100

    """
    def heightChecker(self, heights):
        # return self.heightChecker_common_sort(heights)
        return self.heightChecker_count_sort(heights)

    def heightChecker_count_sort(self, heights):
        """
        Runtime: 16 ms, faster than 96.51% of Python online submissions for Height Checker.
        Memory Usage: 13.5 MB, less than 40.86% of Python online submissions for Height Checker.
        :type heights: List[int]
        :rtype: int
        """
        freq_height = [0] * 101
        for height in heights:
            freq_height[height] += 1
        result = 0
        freq_point = 0

        for height in heights:
            while (freq_height[freq_point] == 0):
                freq_point += 1

            if(freq_height[freq_point] > 0):
                if(height != freq_point):
                    result += 1
                freq_height[freq_point] -= 1
        return result


    def heightChecker_common_sort(self, heights):
        """
        Runtime: 24 ms, faster than 54.25% of Python online submissions for Height Checker.
        Memory Usage: 13.6 MB, less than 5.44% of Python online submissions for Height Checker.
        :type heights: List[int]
        :rtype: int
        """
        excepted = sorted(heights)
        rst_idx_count = 0
        for (idx, item) in enumerate(excepted):
            if(item != heights[idx]):
                rst_idx_count += 1
        return rst_idx_count

    def self_testing(self):
        # 3
        print(self.heightChecker([1,1,4,2,1,3]))
        # 5
        print(self.heightChecker([5,1,2,3,4]))
        # 0
        print(self.heightChecker([1,2,3,4,5]))

Solution().self_testing()