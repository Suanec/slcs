# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

# https://leetcode-cn.com/problems/design-linked-list/
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_list = []



    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if(index < 0 or index >= len(self.index_list)):
            return -1
        else:
            return self.index_list[index].val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        return self.index_list.insert(0,ListNode(val))


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        return self.index_list.append(ListNode(val))


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        return self.index_list.insert(index, ListNode(val))


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if(index < 0 or index >= len(self.index_list)):
            return None
        return self.index_list.pop(index)
