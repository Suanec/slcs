# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/16.

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    """
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



    Example 1:

    Given the following tree [3,9,20,null,null,15,7]:

        3
       / \
      9  20
        /  \
       15   7
    Return true.

    Example 2:

    Given the following tree [1,2,2,3,3,null,null,4,4]:

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.

    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inner_depth_counter(root) >= 0
        # return self.isBalanced_low_effi(root)


    def inner_depth_counter(self, root):
        """
        Runtime: 36 ms, faster than 93.84% of Python online submissions for Balanced Binary Tree.
        Memory Usage: 17.3 MB, less than 78.54% of Python online submissions for Balanced Binary Tree.
        :param root:
        :return:
        """
        if(None == root):
            return 0
        left_depth = self.inner_depth_counter(root.left)
        if(left_depth < 0):
            return -1
        right_depth = self.inner_depth_counter(root.right)
        if(right_depth < 0):
            return -1
        if(abs(left_depth - right_depth) > 1):
            return -1
        return max(left_depth, right_depth) + 1

    def isBalanced_low_effi(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Runtime: 76 ms, faster than 15.91% of Python online submissions for Balanced Binary Tree.
        Memory Usage: 17.5 MB, less than 49.02% of Python online submissions for Balanced Binary Tree.
        """
        if(None == root):
            return True
        if(abs(self.tree_height(root.left) - self.tree_height(root.right)) > 1):
            return False
        return self.isBalanced_low_effi(root.left) and self.isBalanced_low_effi(root.right)

    def tree_height(self, root):
        if(None == root):
            return 0
        return max(self.tree_height(root.left), self.tree_height(root.right)) + 1

    def self_testing(self):
        print self.isBalanced_low_effi(initFullBinaryTree("[3,9,20,null,null,15,7]"))
        print self.isBalanced_low_effi(initFullBinaryTree("[1,2,2,3,3,null,null,4,4]"))
        print self.isBalanced_low_effi(initFullBinaryTree("[1,null,2,null,3]"))
        print "---"
        print self.isBalanced(initFullBinaryTree("[3,9,20,null,null,15,7]"))
        print self.isBalanced(initFullBinaryTree("[1,2,2,3,3,null,null,4,4]"))
        print self.isBalanced(initFullBinaryTree("[1,null,2,null,3]"))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
