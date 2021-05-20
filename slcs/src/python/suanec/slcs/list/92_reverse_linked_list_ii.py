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
    92. Reverse Linked List II
    Medium

    3658

    192

    Add to List

    Share
    Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



    Example 1:


    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    Example 2:

    Input: head = [5], left = 1, right = 1
    Output: [5]


    Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n


    Follow up: Could you do it in one pass?
    """

    def reverseBetween(self, head, left, right):
        """
        Runtime: 20 ms, faster than 60.73% of Python online submissions for Reverse Linked List II.
        Memory Usage: 13.7 MB, less than 56.35% of Python online submissions for Reverse Linked List II.
        :type head: ListNode
        :param left: Int
        :param right: Int
        :return: ListNode
        """
        if(None == head.next):
            return head
        if(left == right):
            return head
        counter = 1
        left_pointer = right_pointer = head
        while(counter < right):
            if(counter < left):
                left_pointer = left_pointer.next
            if(counter < right):
                right_pointer = right_pointer.next
            counter += 1
        return self.reverseBetween_pointer(head, left_pointer, right_pointer)

    def reverseBetween_pointer(self, head, left, right):
        """
        :type head: ListNode
        :type left: ListNode
        :type right: ListNode
        :rtype: ListNode
        """
        if(None == head.next):
            return head
        if(left == right):
            return head
        left.val, right.val = right.val, left.val
        if(right == left.next):
            return head
        rst = left.next
        if(right == left.next.next):
            return head
        ori = left.next.next
        rst.next = right
        p = left

        while(ori != right):
            p = ori
            ori = ori.next
            p.next = rst
            rst = p

        left.next = rst
        return head

    def self_testing(self):
        l = initList([5])
        self.reverseBetween_pointer(l,l,l)
        l = initList([1,2,3,4,5])
        self.reverseBetween_pointer(l, l.next, l.next.next.next.next)
        l = initList([1,2,3,4,5])
        self.reverseBetween(l, 2, 4)
        l = initList([1,2,3,4,5])
        self.reverseBetween(l, 2, 5)

Solution().self_testing()