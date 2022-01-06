# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search_wrong(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums) < 1):
            return -1
        low = 0
        high = len(nums) -1
        mid = (high + low) >> 1
        if(nums[low] == target):
            return low
        if(nums[high] == target):
            return high
        while(low <= high):
            if(target == nums[mid]):
                return mid
            elif(nums[low] < nums[mid]):
                if(nums[mid] > target and nums[low] <= target):
                    high = mid - 1
                    mid = (high + low) >> 1
                else:
                    low = mid + 1
                    mid = (high + low) >> 1
            else:
                if(nums[mid] < target and nums[high] >= target):
                    low = mid + 1
                    mid = (high + low) >> 1
                else:
                    high = mid - 1
                    mid = (high + low) >> 1
        return -1

    def search(self, nums, target):
        low = 0
        high = len(nums) -1

        while(low <= high):
            mid = (high + low) >> 1
            if(target == nums[mid]):
                return mid
            if(nums[low] <= nums[mid]):
                if(target < nums[mid] and target >= nums[low]):
                    high = mid -1
                else:
                    low = mid + 1
            if(nums[mid] <= nums[high]):
                if(target > nums[mid] and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid -1
        return -1;

    def self_testing(self):
        # Output: 4
        print(self.search(nums = [4,5,6,7,0,1,2], target = 0))
        # Output: -1
        print(self.search(nums = [4,5,6,7,0,1,2], target = 3))
        # Output: 1
        print(self.search(nums = [1,3], target = 3))
        # Output: 1
        print(self.search(nums = [3,1], target = 1))
        # Output: -1
        print(self.search(nums = [], target = 5))
        # Output: 1
        print(self.search(nums = [5,1,2,3,4], target= 1))

if __name__ == '__main__':
    Solution().self_testing()
