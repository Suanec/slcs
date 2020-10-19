# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/19. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        Runtime: 24 ms, faster than 90.35% of Python online submissions for Delete Node in a Linked List.
        Memory Usage: 13.7 MB, less than 35.02% of Python online submissions for Delete Node in a Linked List.
        """
        temp = node.next
        node.val = temp.val
        node.next = temp.next
        temp = None