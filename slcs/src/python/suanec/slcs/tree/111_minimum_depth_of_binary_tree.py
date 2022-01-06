# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/18. 
from suanec.slcs.utils.tree_utils import *

class Solution(object):
    """
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.

    """
    MAX_INT = 999999
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Runtime: 40 ms, faster than 44.71% of Python online submissions for Minimum Depth of Binary Tree.
        Memory Usage: 15.5 MB, less than 83.04% of Python online submissions for Minimum Depth of Binary Tree.
        """
        if(None == root):
            return 0
        return self.inner_depth_count(root)

    def inner_depth_count(self, root):
        if(None == root):
            return self.MAX_INT
        left_depth = self.inner_depth_count(root.left)
        right_depth = self.inner_depth_count(root.right)
        sub_depth = min(left_depth, right_depth)
        cur_depth = sub_depth + 1 if(sub_depth < self.MAX_INT) else 1
        return  cur_depth

    def self_testing(self):
        print(self.minDepth(initFullBinaryTree("[3,9,20,null,null,15,7]")))
        print(self.minDepth(initFullBinaryTree("[1,2]")))

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
