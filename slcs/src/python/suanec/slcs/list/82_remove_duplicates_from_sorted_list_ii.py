# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.list_utils import *
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution(object):
    def removeSingleListNode(self, node, head):
        if(not node):
            return
        if(head == node and not head.next):
            return (None,None)
        if(node.next):
            tmp = node.next
            node.next = tmp.next
            node.val = tmp.val
            return (head,node)
        else:
            tmp = head
            while(tmp.next != node):
                tmp = tmp.next
            tmp.next = node.next
            node = None
            return (head,node)

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):
            return head
        if(not head.next):
            return head

        cur_node = head
        # definition key:value pointer.val: (pointer, isalive)
        known_node_dict = {}
        while(cur_node):
            if(not known_node_dict.has_key(cur_node.val)):
                known_node_dict[cur_node.val] = (cur_node,True)
                cur_node = cur_node.next
            else:
                known_node = known_node_dict.get(cur_node.val)
                if(known_node[1]):
                    if(known_node[0].next == cur_node ):
                        (head,cur_node) = self.removeSingleListNode(known_node[0], head)
                    else:
                        (head,cur) = self.removeSingleListNode(known_node[0], head)
                    known_node_dict[known_node[0].val] = (known_node[0],False)

                (head,cur_node) = self.removeSingleListNode(cur_node, head)
        return head

    def self_testing(self):

        source = [1,2,3,4,5]
        s = Solution()

        head = initList(source)
        node = head
        s.removeSingleListNode(node, head)

        head = initList(source)
        node = head.next.next
        s.removeSingleListNode(node, head)

        head = initList(source)
        node = head.next.next.next.next
        s.removeSingleListNode(node, head)

        head = initList([1,2,3,3,4,4,5])
        s.deleteDuplicates(head)
        head = initList([1,1])
        s.deleteDuplicates(head)
        head = initList([1,2,3,4,4,4,4])
        s.deleteDuplicates(head)
