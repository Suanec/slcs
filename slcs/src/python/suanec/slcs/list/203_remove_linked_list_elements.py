# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/19.
from suanec.slcs.utils.list_utils import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    '''
    Remove all elements from a linked list of integers that have value val.

    Example:

    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
    '''
    def removeElements(self, head, val):
        """
        Runtime: 60 ms, faster than 84.26% of Python online submissions for Remove Linked List Elements.
        Memory Usage: 20.3 MB, less than 7.23% of Python online submissions for Remove Linked List Elements.
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if(not head):
            return head
        while(head and head.val == val):
            head = head.next
        if(not head):
            return head
        p_pre = head
        p_cur = p_pre.next
        while(p_cur):
            if(p_cur.val == val):
                p_pre.next = p_cur.next
                p_cur = p_pre.next
            else:
                p_pre = p_pre.next
                p_cur = p_cur.next
        return head

    def self_testing(self):
        printList(self.removeElements(initList([1,2,6,3,4,5,6]), 6))
        printList(self.removeElements(initList([1,1,1,2,6,3,4,5,6]), 1))
        printList(self.removeElements(initList([]), 1))
        printList(self.removeElements(initList([2,3]), 1))
        printList(self.removeElements(initList([1,1,1,1,1]), 1))

if __name__ == '__main__':
    Solution().self_testing()

