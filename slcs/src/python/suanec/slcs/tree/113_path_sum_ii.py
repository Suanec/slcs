# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

from suanec.slcs.utils.tree_utils import *

# https://leetcode-cn.com/problems/path-sum-ii/
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        path_sum = self.pathAndSum(root)
        for x in path_sum:
            x[1].reverse()

        return [x[1] for x in path_sum if (x[0] == sum)]

    def pathAndSum(self, root):
        if(not root):
            return []
        left_sum = self.pathAndSum(root.left)
        right_sum = self.pathAndSum(root.right)
        rst_sum = left_sum + right_sum
        if(len(rst_sum) < 1):
            return [(root.val, [root.val])]
        return [(x[0] + root.val, x[1] + [root.val]) for x in rst_sum]

    def self_testing(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        s = Solution()
        # print(s.pathSum(root,22))

