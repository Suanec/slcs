# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# https://leetcode-cn.com/problems/h-index/
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if(len(citations) < 1):
            return 0
        if(len(citations) == 1):
            return 1
