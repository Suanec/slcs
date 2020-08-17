# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# https://leetcode-cn.com/problems/invert-binary-tree/
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root == None):
            return root
        ori_left = self.invertTree(root.left)
        ori_right = self.invertTree(root.right)
        root.right = ori_left
        root.left = ori_right
        return root

