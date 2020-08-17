# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.tree_utils import *

# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
        if(not root.left and not root.right):
            return root.val
        sub_sum = self.sumSubNumbers(root, 0)
        return sum(sub_sum)

    def sumSubNumbers(self, root, parent_sum):
        """
        :type root: TreeNode
        :rtype: list[int]
        """
        if(not root):
            return []
        left_sum_list = self.sumSubNumbers(root.left, parent_sum * 10 + root.val)
        right_sum_list = self.sumSubNumbers(root.right, parent_sum * 10 + root.val)
        leaf_list = left_sum_list + right_sum_list
        if(len(leaf_list) < 1):
            return [parent_sum * 10 + root.val]

        return leaf_list

    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        print self.sumNumbers(root)
        # [4,9,0,5,1]
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        print self.sumNumbers(root)

# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
        if(not root.left and not root.right):
            return root.val
        sub_sum = self.sumSubNumbers(root, 0)
        return sum(sub_sum)

    def sumSubNumbers(self, root, parent_sum):
        """
        :type root: TreeNode
        :rtype: list[int]
        """
        if(not root):
            return []
        left_sum_list = self.sumSubNumbers(root.left, parent_sum * 10 + root.val)
        right_sum_list = self.sumSubNumbers(root.right, parent_sum * 10 + root.val)
        leaf_list = left_sum_list + right_sum_list
        if(len(leaf_list) < 1):
            return [parent_sum * 10 + root.val]

        return leaf_list

    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        print self.sumNumbers(root)
        # [4,9,0,5,1]
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        print self.sumNumbers(root)


if __name__ == '__main__':

    s = Solution()
    s.self_testing()
