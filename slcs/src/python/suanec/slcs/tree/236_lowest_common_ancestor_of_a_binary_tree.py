# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

from suanec.slcs.utils.tree_utils import *

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution(object):
    '''
    236. Lowest Common Ancestor of a Binary Tree
    Medium

    4419

    185

    Add to List

    Share
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



    Example 1:


    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    Example 2:


    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    Example 3:

    Input: root = [1,2], p = 1, q = 2
    Output: 1


    Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rst_set = {p.val, q.val}
        return self.innerLowestCommonAncestor(root, rst_set)

    def innerLowestCommonAncestor(self, root, _rst_set):
        if(not root):
            return None

        left_target = self.innerLowestCommonAncestor(root.left, _rst_set)
        right_target = self.innerLowestCommonAncestor(root.right, _rst_set)
        if(root.val in _rst_set):
            return root
        elif(left_target and right_target):
            return root
        elif(left_target):
            return left_target
        elif(right_target):
            return right_target
        else:
            return None


    def self_testing(self):
        '''
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6
        Explanation: The LCA of nodes 2 and 8 is 6.
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        Output: 2
        Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
        :return:
        '''
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        print self.lowestCommonAncestor(root, root.left, root.right).__dict__.get("val")
        print self.lowestCommonAncestor(root, root.left, root.left.right).__dict__.get("val")
