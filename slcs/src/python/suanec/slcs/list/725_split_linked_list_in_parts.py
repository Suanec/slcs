# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode-cn.com/problems/split-linked-list-in-parts/
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if(root == None):
            rst = [None for x in range(0,k)]
            return rst
        if(root.next == None):
            rst = [None for x in range(0,k)]
            rst[0] = root
            return rst
        cur_tail = root
        count = 0
        while(cur_tail != None):
            cur_tail = cur_tail.next
            count += 1
        cur_tail = root
        bucket_base = count / k
        bucket_buffer = count % k
        rst = [None for x in range(0,k)]
        pre_tail = cur_tail
        for i in range(0, bucket_buffer):
            # rst[i].append(cur_tail)
            rst[i] = cur_tail
            tmp_count = bucket_base
            while(tmp_count > 0):
                cur_tail = cur_tail.next
                tmp_count -= 1
            pre_tail = cur_tail
            cur_tail = cur_tail.next
            pre_tail.next = None
        for i in range(bucket_buffer,k):
            if(cur_tail):
                # rst[i].append(cur_tail)
                rst[i] = cur_tail
                tmp_count = bucket_base -1
                while(tmp_count > 0):
                    cur_tail = cur_tail.next
                    tmp_count -= 1
                pre_tail = cur_tail
                cur_tail = cur_tail.next
                pre_tail.next = None
        return rst
