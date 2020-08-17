# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.


# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/submissions/
class Solution(object):
    def search_brute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.__contains__
        nums.__eq__("")
        return target in nums
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) -1
        while(low <= high):
            mid = (high + low) >> 1
            if(target == nums[mid]):
                return True
            if(nums[low] <= nums[mid]):
                if(target < nums[mid] and target >= nums[low]):
                    high = mid -1
                else:
                    low = mid + 1
            elif(nums[mid] <= nums[high]):
                if(target > nums[mid] and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid -1
        return False

    def self_testing(self):
        print self.search(nums = [2,5,6,0,0,1,2], target = 0)
        print self.search( nums = [2,5,6,0,0,1,2], target = 3)
        print self.search( nums = [1,1,3,1] , target=3)

if __name__ == '__main__':
    Solution().self_testing()
