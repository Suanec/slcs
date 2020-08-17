# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        h = dummy_head
        while(h.next):
            p = h.next
            q = p
            sum = p.val
            while(q.next or not sum):
                if(not sum):
                    h.next = q.next
                    break
                q = q.next
                sum += q.val

            if(sum): h = h.next
        return dummy_head.next