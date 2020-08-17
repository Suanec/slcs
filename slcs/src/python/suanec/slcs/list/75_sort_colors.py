# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# https://leetcode.com/problems/sort-colors/
class Solution(object):
    '''
    Runtime: 8 ms, faster than 100.00% of Python online submissions for Sort Colors.
    Memory Usage: 12.6 MB, less than 5.13% of Python online submissions for Sort Colors.
    Next challenges:
    '''
    def swap(self, nums, i, j):
        if(i == j):return
        nums[i] += nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    def sortColors_self(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_suffix = 0
        while(zero_suffix < len(nums) and nums[zero_suffix] == 0):
            zero_suffix += 1
        if(zero_suffix == len(nums) ): return # nums

        two_prefix = len(nums) -1
        while(two_prefix > 0 and nums[two_prefix] == 2):
            two_prefix -= 1
        if(two_prefix == 0): return # nums

        if(zero_suffix >= two_prefix): return
        if(nums[zero_suffix] > nums[two_prefix]):
            self.swap(nums, zero_suffix, two_prefix)
        p= zero_suffix + 1
        while(p <= two_prefix and zero_suffix <= two_prefix):
            if(nums[p] == 0):
                self.swap(nums, zero_suffix, p)
                while(nums[zero_suffix] == 0):
                    zero_suffix += 1
                    if(p < zero_suffix):
                        p = zero_suffix
            elif(nums[p] == 2):
                self.swap(nums, two_prefix, p)
                while(nums[two_prefix] == 2):
                    two_prefix -=1
            elif(nums[p] == 1):
                p += 1
                # return nums

    def sortColors(self, nums):
        r = w = b = 0;
        for i in range(0,len(nums)):
            if(nums[i]==0):
                nums[b] = 2
                nums[w] = 1
                nums[r] = 0
                b+= 1; w+=1; r+=1;
            elif(nums[i]==1):
                nums[b] = 2
                nums[w] = 1
                b+= 1; w+=1;
            elif(nums[i]==2):
                b+= 1
        return nums

    def self_testing(self):
        # Output: [0,0,1,1,2,2]
        print self.sortColors(nums= [0,0,0,0,0,0])
        print self.sortColors(nums= [2,2,2,2,2,2])
        print self.sortColors(nums= [2,0,2,1,1,0])
        print self.sortColors(nums= [2,0,0,0,0,0])
        print self.sortColors(nums= [1,0,0,0,0,0])
        print self.sortColors(nums= [])
        print self.sortColors(nums= [2, 1])
        print self.sortColors(nums= [2, 0])
        print self.sortColors(nums= [1, 0])
        print self.sortColors(nums= [0, 1])
        print self.sortColors(nums= [0, 0, 2])
        pass

if __name__ == '__main__':
    Solution().self_testing()