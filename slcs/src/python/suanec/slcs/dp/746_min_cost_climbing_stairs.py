# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if(len(cost) < 2):
            return 0
        rst = [i for i in cost]
        for i in xrange(2, len(cost)):
            rst[i] += min(rst[i-1], rst[i-2])
        return min(rst[-1], rst[-2])


    def self_testing(self):
        cost = [10, 15, 20] # Output: 15
        s = Solution()
        print s.minCostClimbingStairs(cost)
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] # Output: 6
        s = Solution()
        print s.minCostClimbingStairs(cost)


s = Solution()
s.self_testing()
