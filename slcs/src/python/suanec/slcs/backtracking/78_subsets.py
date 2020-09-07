# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/7. 

class Solution(object):
    """
    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    """
    def subsets(self, nums):
        # return self.subsets_native(nums)
        return self.subsets_dp(nums)

    def subsets_native(self, nums):
        """
        Runtime: 24 ms, faster than 67.65% of Python online submissions for Subsets.
        Memory Usage: 13 MB, less than 7.71% of Python online submissions for Subsets.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        if(len(nums) < 1):return result
        for idx in xrange(0, len(nums)):
            cur = nums[idx]
            rst = []
            sub_rst = self.subsets(nums[idx + 1:])
            for subset in sub_rst:
                subset.append(cur)
                # rst.append(subset)
            rst += sub_rst
            result += rst
        return result

    def subsets_dp(self, nums):
        """
        Runtime: 20 ms, faster than 84.70% of Python online submissions for Subsets.
        Memory Usage: 12.8 MB, less than 44.97% of Python online submissions for Subsets.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        if(len(nums) < 1):return results
        global_dict = {}

        for cur_p in nums:
            result = []
            rst = []
            for (num_key, sub_set) in global_dict.items():
                rst = []
                [rst.append(list(x)) for x in sub_set]
                for i in rst:
                    i.append(cur_p)
                result += rst
            # result.append([])
            result.append([cur_p])
            global_dict[cur_p] = result
            results += result
        return results

    def self_testing(self):
        nums = [1,2,3]
        print self.subsets(nums)

if __name__ == '__main__':
    s = Solution()
    s.self_testing()