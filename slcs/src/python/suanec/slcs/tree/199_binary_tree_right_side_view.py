# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/4. 

from suanec.slcs.utils.tree_utils import *


from collections import deque
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
        print(q)
        print(q.pick())
        print(q.pick(2))
        print(q.get())
        print(q)

class Solution(object):
    """
    Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Example:

    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
    Explanation:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    """
    def rightSideView(self, root):
        """
        Runtime: 16 ms, faster than 93.46% of Python online submissions for Binary Tree Right Side View.
        Memory Usage: 12.5 MB, less than 99.83% of Python online submissions for Binary Tree Right Side View.
        :type root: TreeNode
        :rtype: List[int]
        """
        level_order_seq = self.level_order_sperate(root)
        return [x[-1] for x in level_order_seq if(len(x) > 0)]

    def level_order_sperate(self, root):
        if(None == root):
            return [[]]
        q = queue()
        rst = []
        level_rst = []
        level_flag = 0
        q.push((root,1))
        while(not q.empty()):
            (node, level) = q.pop()
            if(node.left):
                q.push((node.left, level + 1))
            if(node.right):
                q.push((node.right, level + 1))
            if(level != level_flag):
                rst.append(level_rst)
                level_rst = []
                level_flag = level
            level_rst.append(node.val)
        if(len(level_rst) > 0):
            rst.append(level_rst)
        return rst




    def self_testing(self):
        root = initFullBinaryTree("[1,2,3,null,5,null,4]")
        print(self.rightSideView(root))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
