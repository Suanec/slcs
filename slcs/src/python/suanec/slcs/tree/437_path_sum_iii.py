# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

from suanec.slcs.utils.tree_utils import *

# https://leetcode-cn.com/problems/path-sum-iii/
class Solution(object):
    cnt = 0
    sum = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if(not root):
            return 0
        path_sum = self.pathAndSum(root)
        # for x in path_sum:
        #     x[1].reverse()
        print path_sum

        return len([x for x in path_sum if (x == sum)])

    def pathAndSum(self, root):
        if(not root):
            # cur_path, node_path, sum_path
            # cur_layer, sub_layer, sum_layer
            return [0]
        left_sum = self.pathAndSum(root.left)
        right_sum = self.pathAndSum(root.right)
        if(len(left_sum + right_sum) < 1):
            return [root.val]

        rst_sum = [
            root.val + x for x in left_sum + right_sum
        ]

        len([x for x in rst_sum if x == self.sum])
        return [[root.val], rst_sum[1].append(root.val), [x + root.val for x in rst_sum[2]]]

    def self_testing(self):
        root = TreeNode(10)

        root.left = TreeNode(5)
        root.right = TreeNode(-3)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)

        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)

        root.left.right.right = TreeNode(1)

        root.right.right = TreeNode(11)
        print self.pathSum(root, 8)

