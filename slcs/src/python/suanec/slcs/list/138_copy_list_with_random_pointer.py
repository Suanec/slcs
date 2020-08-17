# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if(not head):
            return head
        if(not head.next):
            new_head = Node(head.val, head.next, None)
            if(head.random):
                new_head.random = new_head
            return new_head
        new_head = Node(head.val, None, None)
        ori_header = head
        new_header = new_head
        node_map = {ori_header: new_header}
        while(ori_header.next):
            new_node  = Node(ori_header.next.val, None, None)
            node_map[ori_header.next] = new_node
            new_header.next = new_node
            ori_header = ori_header.next
            new_header = new_header.next
        ori_header = head
        new_header = new_head
        while(ori_header):
            new_header.random = node_map.get(ori_header.random)
            ori_header = ori_header.next
            new_header = new_header.next
        return new_head
    def self_testing(self):

        # {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
        head = Node(1,None, None)
        sec = Node(2,None, None)
        head.next = sec
        head.random = sec
        sec.random = sec
        s = Solution()
        # {"$id":"1","next":{"$id":"2","next":null,"random":null,"val":1},"random":null,"val":-1}
        head = Node(-1,None, None)
        sec = Node(1,None, None)
        # head.next = sec
        head.random = head
        s.copyRandomList(head)
