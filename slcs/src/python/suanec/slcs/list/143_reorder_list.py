# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode-cn.com/problems/reorder-list/
class Solution(object):
    def reverseList(self, head):
        if(head == None ):
            return head
        if(head.next == None):
            return head
        cur = head.next
        rst = None
        rst_head = head
        rst_head.next = None
        while(cur):
            rst = cur
            cur = cur.next
            rst.next = rst_head
            rst_head = rst
        return rst_head



    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if(head == None or head.next == None):
            return head
        cur_tail = head
        count = 0
        while(cur_tail != None):
            cur_tail = cur_tail.next
            count += 1
        half_tail_count = count / 2
        if(count % 2 != 0):
            half_tail_count += 1
        head_tail = head
        for i in xrange(1, half_tail_count):
            head_tail = head_tail.next
        tail_head = head_tail.next
        head_tail.next = None
        tail_head = self.reverseList(tail_head)
        main_cur = head
        tail_cur = tail_head
        while(tail_cur):
            main_next = main_cur.next
            tail_next = tail_cur.next
            main_cur.next = tail_cur
            tail_cur.next = main_next
            main_cur = main_next
            tail_cur = tail_next
        return head
    def self_testing(self):
        reverse_test = [1,2,3,4,5,6,7,8]
        s = Solution()
        # printList(s.reverseList(initList(reverse_test)))
        reorder_test = [1,2,3,4,5]
        s = Solution()
        # printList(s.reorderList(initList(reorder_test)))
