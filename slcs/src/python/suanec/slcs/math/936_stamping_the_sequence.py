# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# https://leetcode-cn.com/problems/stamping-the-sequence/
class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        rst = []
        if(len(target) < len(stamp)):
            return rst
        if(target[0] != stamp[0]):
            return rst
        if(target[-1] != stamp[-1]):
            return rst
        max_retry = 10 * len(target)