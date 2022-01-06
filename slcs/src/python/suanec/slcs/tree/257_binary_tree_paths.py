# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.tree_utils import *

# https://leetcode-cn.com/problems/binary-tree-paths/
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.binaryTreePath(root, "")

    def binaryTreePath(self, root, path):
        if(not root):
            return []
        if(len(path)>0):
            child_path = path + "->" + str(root.val)
        else:
            child_path = str(root.val)
        left_path = self.binaryTreePath(root.left, child_path)
        right_path = self.binaryTreePath(root.right, child_path)
        child_paths = left_path + right_path
        return child_paths if(len(child_paths)>0) else [child_path]

    def self_testing(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        s = Solution()
        # print(s.binaryTreePaths(root))

