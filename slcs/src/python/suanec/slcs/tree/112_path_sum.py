# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.tree_utils import *

# https://leetcode-cn.com/problems/path-sum/
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(not root):
            return False
        path_sum = self.pathSum(root)
        return sum in path_sum

    def pathSum(self, root):
        if(not root):
            return []
        left_sum = self.pathSum(root.left)
        right_sum = self.pathSum(root.right)
        rst_sum = left_sum + right_sum
        if(len(rst_sum) < 1):
            return [root.val]
        return [x + root.val for x in left_sum + right_sum]

    def self_testing(self):

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        s = Solution()
        # root = TreeNode(1)
        # root.left = TreeNode(2)
        # print s.hasPathSum(root,22)

