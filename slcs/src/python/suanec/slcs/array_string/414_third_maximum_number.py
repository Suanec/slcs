# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/4/30. 

class Solution(object):
    """
    414. Third Maximum Number
    Easy

    988

    1711

    Add to List

    Share
    Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.



    Example 1:

    Input: nums = [3,2,1]
    Output: 1
    Explanation: The third maximum is 1.
    Example 2:

    Input: nums = [1,2]
    Output: 2
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
    Example 3:

    Input: nums = [2,2,3,1]
    Output: 1
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.


    Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


    Follow up: Can you find an O(n) solution?

    """
    def thirdMax(self, nums):
        """
        Runtime: 36 ms, faster than 78.35% of Python online submissions for Third Maximum Number.
        Memory Usage: 14.4 MB, less than 58.88% of Python online submissions for Third Maximum Number.
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if(len_nums == 0):
            return 0
        elif(len_nums == 1):
            return nums[0]
        elif(len_nums == 2):
            return nums[0] if nums[0] > nums[1] else nums[1]
        third_max = second_max = first_max = -9e99
        for elem in nums:
            if(elem > first_max):
                third_max, second_max = second_max, first_max
                first_max = elem
            elif(elem == first_max):
                pass
            elif(elem > second_max):
                third_max = second_max
                second_max = elem
            elif(elem == second_max):
                pass
            elif(elem > third_max):
                third_max = elem
        return third_max if third_max > -9e99 else first_max

    def self_testing(self):
        print(self.thirdMax([3,2,1]))
        print(self.thirdMax([2,1]))
        print(self.thirdMax([2,2,3,1]))
        print(self.thirdMax([1023,2,3,1]))

Solution().self_testing()


