# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/6. 
class Solution(object):
    """
    628. Maximum Product of Three Numbers
    Easy

    1616

    448

    Add to List

    Share
    Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



    Example 1:

    Input: nums = [1,2,3]
    Output: 6
    Example 2:

    Input: nums = [1,2,3,4]
    Output: 24
    Example 3:

    Input: nums = [-1,-2,-3]
    Output: -6


    Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
    Accepted
    152,297
    Submissions
    325,767
    """
    def maximumProduct(self, nums):
        """
        Runtime: 208 ms, faster than 97.41% of Python online submissions for Maximum Product of Three Numbers.
        Memory Usage: 14.7 MB, less than 39.66% of Python online submissions for Maximum Product of Three Numbers.
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 3):
            return nums[0] * nums[1] * nums[2]

        max_1 = float('-inf')
        max_2 = float('-inf')
        max_3 = float('-inf')
        min_1 = float('inf')
        min_2 = float('inf')
        for num in nums:
            for elem in nums:
                if(elem > max_1):
                    max_3, max_2, max_1 = max_2, max_1, elem
                elif(elem > max_2):
                    max_3, max_2 = max_2, elem
                elif(elem > max_3):
                    max_3 = elem

                if(elem < min_1):
                    min_2, min_1 = min_1, elem
                elif(elem < min_2):
                    min_2 = elem

            return max( max_1 * max_2 * max_3, max_1 * min_1 * min_2)


    def maximumProduct_self(self, nums):
        """

        Runtime: 220 ms, faster than 68.10% of Python online submissions for Maximum Product of Three Numbers.
        Memory Usage: 14.9 MB, less than 8.33% of Python online submissions for Maximum Product of Three Numbers.
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 3):
            return nums[0] * nums[1] * nums[2]
        positive_part = []
        negative_part = []
        for num in nums:
            if(num >= 0):
                positive_part.append(num)
            elif(num < 0):
                negative_part.append(num)
        if(len(negative_part) < 2 or len(positive_part) < 1):
            first_max = float('-inf')
            second_max = float('-inf')
            third_max = float('-inf')
            for elem in nums:
                if(elem > first_max):
                    third_max, second_max, first_max = second_max, first_max, elem
                elif(elem > second_max):
                    third_max, second_max = second_max, elem
                elif(elem > third_max):
                    third_max = elem

            return first_max * second_max * third_max
        else:
            pos_max_1 = float('-inf')
            pos_max_2 = float('-inf')
            pos_max_3 = float('-inf')
            for elem in positive_part:
                if(elem > pos_max_1):
                    pos_max_3, pos_max_2, pos_max_1 = pos_max_2, pos_max_1, elem
                elif(elem > pos_max_2):
                    pos_max_3, pos_max_2 = pos_max_2, elem
                elif(elem > pos_max_3):
                    pos_max_3 = elem

            neg_min_1 = float('inf')
            neg_min_2 = float('inf')
            neg_min_3 = float('inf')
            for elem in negative_part:
                if(elem < neg_min_1):
                    neg_min_3, neg_min_2, neg_min_1 = neg_min_2, neg_min_1, elem
                elif(elem < neg_min_2):
                    neg_min_3, neg_min_2 = neg_min_3, elem
                elif(elem < neg_min_3):
                    neg_min_3 = elem

            neg_part = neg_min_1 * neg_min_2
            pos_part = pos_max_2 * pos_max_3

            first_position = pos_max_1 if(pos_max_1 >= 0) else neg_min_3
            return first_position * (neg_part if (neg_part > pos_part or pos_part == float('inf')) else pos_part)

    def self_testing(self):
        print(self.maximumProduct([1,2,3]))
        print(self.maximumProduct([1,2,3,4]))
        print(self.maximumProduct([-1,-2,-3]))
        print(self.maximumProduct([-100,-98,-1,2,3,4]))
        print(self.maximumProduct([0,0,-1,0]))
        print(self.maximumProduct([-100,-2,-3,1]))
        print(self.maximumProduct([-1,-2,1,2,3]))
        print(self.maximumProduct([-3,-2,-1,0,0,0,0]))
        print(self.maximumProduct([-1,-2,-3,-4] ))

Solution().self_testing()
