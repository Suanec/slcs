# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from collections import deque
# #############     BINARY TREE     # #############
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class stack(deque):
    def push(self, x):
        self.append(x)

    def pick(self):
        return self[-1]

    def empty(self):
        return len(self) == 0

    def self_testing(self):

        s = stack()
        s.push(5);s.push(3);s.push(4);s.push(5)
        print s
        print s.pick()
        print s.pop()
        print s

class queue(deque):
    def push(self, x):
        self.append(x)

    def pick(self, idx = 0):
        return self[idx] if(len(self) > idx) else None

    def empty(self):
        return len(self) == 0

    def pop(self):
        return self.popleft()

    def get(self):
        tmp = self[0]
        self.remove(tmp)
        return tmp

    def self_testing(self):
        q = queue()
        q.push(5);q.push(3);q.push(4);q.push(5)
        # print q
        # print q.pick();print q.pick(2)
        # print q.get()

def initFullBinaryTree(source = []):
    if(len(source) < 0):
        return None
    q = queue(maxsize=len(source))
    node_sum = len(source) -1
    for i in source:
        q.put((i,0))
    # root =
    while(not q.empty()):
        pass

