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
        s.push(5);s.push(3);s.push(4);s.push(1)
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
        q.push(5);q.push(3);q.push(4);q.push(51)
        print q
        print q.pick()
        print q.pick(2)
        print q.get()
        print q

def initFullBinaryTree(source ="[5,4,1,null,1,null,4,2,null,2,null]"):
    _source = eval(source.replace("null", "None"))
    source_len = len(_source)
    if(source_len < 0):
        return None
    root = TreeNode(_source[0])
    if(source_len % 2 == 0):
        _source.append(None)
    q = queue()
    q.push(root)
    for i in xrange(1,source_len,2):
        cur_left_val = None if(_source[i] == None) else TreeNode(_source[i])
        cur_right_val = None if(_source[i + 1] == None) else TreeNode(_source[i + 1])
        cur = q.get()
        if(None != cur_left_val):
            q.push(cur_left_val)
        if(None != cur_right_val):
            q.push(cur_right_val)
        cur.left = cur_left_val
        cur.right = cur_right_val
    return root

def middle_print(root):
    def middle_order(root):
        res = []
        if(None == root): return res
        res += middle_order(root.left)
        res.append(root.val)
        res += middle_order(root.right)
        return res
    middle_order_seq = middle_order(root)
    print middle_order_seq

def level_print(root):
    def level_order(root):
        res = []
        if(None == root): return res
        q = queue()
        q.push(root)
        while(not q.empty()):
            cur = q.get()
            cur_val = None if(None == cur) else cur.val
            res.append(cur_val)
            if(None != cur):
                q.push(cur.left)
                q.push(cur.right)
        return res
    level_order_seq = level_order(root)
    print level_order_seq

if __name__ == '__main__':
    q = queue()
    q.self_testing()
    is_symmetric_source = initFullBinaryTree("[5,4,1,null,1,null,4,2,null,2,null]")
    middle_print(is_symmetric_source)
    level_print(is_symmetric_source)

