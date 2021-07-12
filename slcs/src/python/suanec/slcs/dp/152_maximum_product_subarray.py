# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/7/12. 

class Solution(object):
    '''
    Given an integer array nums,
    find a contiguous non-empty subarray within the array that has the largest product,
    and return the product.

    It is guaranteed that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.



    Example 1:

    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    Example 2:

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


    Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    '''
    def maxProduct(self, nums):
        """
        Runtime: 40 ms, faster than 64.56% of Python online submissions for Maximum Product Subarray.
        Memory Usage: 13.9 MB, less than 64.78% of Python online submissions for Maximum Product Subarray.

        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        cur_max = float("-inf")
        product = 1
        for i in nums:
            product *= i
            cur_max = max(cur_max, product)
            if(0 == i):
                product = 1
        product = 1
        for j in reversed(nums):
            product *= j
            cur_max = max(cur_max, product)
            if(0 == j):
                product = 1
        return cur_max



    def self_testing(self):
        print(self.maxProduct([1,2,3,0,4]))
        print(self.maxProduct([1,2,3,-4,-5,-6,7]))
        print(self.maxProduct([1,2,3,4,-5,-6,7]))
        print(self.maxProduct([2,3,-2,4]))
        print(self.maxProduct([-2,0,-1]))
        print(self.maxProduct([]))
        print(self.maxProduct([0]))
        print(self.maxProduct([23]))

Solution().self_testing()