# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/20.

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    '''
    98. Validate Binary Search Tree
    Medium

    4655

    578

    Add to List

    Share
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


    Example 1:

        2
       / \
      1   3

    Input: [2,1,3]
    Output: true
    Example 2:

        5
       / \
      1   4
         / \
        3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    '''
    def isValidBST(self, root):
        """
        Runtime: 48 ms, faster than 19.79% of Python online submissions for Validate Binary Search Tree.
        Memory Usage: 17.9 MB, less than 61.68% of Python online submissions for Validate Binary Search Tree.
        :type root: TreeNode
        :rtype: bool
        """
        return self.inner_is_valid_bst(root, left_min=float("-inf"), right_max=float("inf"))

    def inner_is_valid_bst(self, root, left_min, right_max):
        if(None == root):
            return True
        if(root.val > left_min and root.val < right_max):
            left_is_valid_bst = self.inner_is_valid_bst(root.left, left_min=left_min, right_max=root.val)
            right_is_valid_bst = self.inner_is_valid_bst(root.right, left_min=root.val, right_max=right_max)
            return left_is_valid_bst and right_is_valid_bst
        else:
            return False

    def self_testing(self):
        print self.isValidBST(initFullBinaryTree("[5,1,4,null,null,3,6]"))
        print self.isValidBST(initFullBinaryTree("[2,1,3]"))


if __name__ == '__main__':
    Solution().self_testing()
