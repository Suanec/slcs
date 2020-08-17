# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 


# https://leetcode-cn.com/problems/odd-even-linked-list/
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return head
        if(head.next == None):
            return head
        odd_head = head
        odd_tail = odd_head
        even_head = head.next
        even_tail = even_head
        while(odd_tail.next and even_tail.next):
            odd_tail.next = even_tail.next
            odd_tail = even_tail.next
            even_tail.next = odd_tail.next
            even_tail = odd_tail.next
        if(not even_tail):
            odd_tail.next = even_head
            return head
        if(even_tail.next != odd_tail):
            odd_tail.next = even_tail.next
            if(even_tail.next):
                odd_tail = even_tail.next
        odd_tail.next = even_head
        return head
    def self_testing(self):
        even_test = [1,2,3,4,5,6,7,8]
        s = Solution()
        # printList(s.oddEvenList(initList(even_test)))