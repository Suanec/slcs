# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/6. 

class Solution(object):
    """

    1464. Maximum Product of Two Elements in an Array
    Easy

    434

    84

    Add to List

    Share
    Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


    Example 1:

    Input: nums = [3,4,5,2]
    Output: 12
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
    Example 2:

    Input: nums = [1,5,4,5]
    Output: 16
    Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
    Example 3:

    Input: nums = [3,7]
    Output: 12


    Constraints:

    2 <= nums.length <= 500
    1 <= nums[i] <= 10^3
    """
    def maxProduct(self, nums):
        """
        Runtime: 28 ms, faster than 98.41% of Python online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 13.5 MB, less than 30.23% of Python online submissions for Maximum Product of Two Elements in an Array.

        Runtime: 36 ms, faster than 64.77% of Python online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 13.4 MB, less than 57.05% of Python online submissions for Maximum Product of Two Elements in an Array.
        :type nums: List[int]
        :rtype: int
        """
        first_max = float('-inf')
        second_max = float('-inf')
        for elem in nums:
            if(elem > first_max):
                second_max, first_max = first_max, elem
            elif(elem > second_max):
                second_max = elem
        return (first_max -1) * (second_max -1)

    def self_testing(self):
        print(self.maxProduct([3,4,5,2]))
        print(self.maxProduct([1,5,4,5]))
        print(self.maxProduct([3,7]))

Solution().self_testing()