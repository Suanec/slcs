# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/19. 
from suanec.slcs.utils.list_utils import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    206. Reverse Linked List
    Easy

    7027

    135

    Add to List

    Share
    Given the head of a singly linked list, reverse the list, and return the reversed list.



    Example 1:


    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Example 2:


    Input: head = [1,2]
    Output: [2,1]
    Example 3:

    Input: head = []
    Output: []


    Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000


    Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseList_recursively(head)[0]
        # return self.reverseList_iteratively(head)

    def reverseList_iteratively(self, head):
        """
        Runtime: 20 ms, faster than 92.09% of Python online submissions for Reverse Linked List.
        Memory Usage: 15.2 MB, less than 92.17% of Python online submissions for Reverse Linked List.
        :param head:
        :return:
        """
        if(None == head):
            return head
        if(None == head.next):
            return head
        ori = head.next
        rst = head
        rst.next = None
        p = head
        while(None != ori):
            p = ori
            ori = ori.next
            p.next = rst
            rst = p
        return rst


    def reverseList_recursively(self, head):
        """
        Runtime: 32 ms, faster than 10.57% of Python online submissions for Reverse Linked List.
        Memory Usage: 18.8 MB, less than 12.36% of Python online submissions for Reverse Linked List.
        :param head:
        :return:
        """
        if(None == head):
            head = None
            last = None
            return (head, last)
        if(None == head.next):
            last = head
            return (head, last)
        (tail_head, tail_last) = self.reverseList_recursively(head.next)
        tail_last.next = head
        head.next = None
        last = head
        return (tail_head, last)


    def self_testing(self):
        printList(self.reverseList( initList([1,2,3,4,5] )))
        printList(self.reverseList( initList([1,2] ))      )
        printList(self.reverseList( initList([] ))         )

Solution().self_testing()