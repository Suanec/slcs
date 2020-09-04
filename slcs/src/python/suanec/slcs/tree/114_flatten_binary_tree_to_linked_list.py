# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/4. 

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    """
    114. Flatten Binary Tree to Linked List
    Medium

    3117

    348

    Add to List

    Share
    Given a binary tree, flatten it to a linked list in-place.

    For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6
    The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
    """
    def flatten(self, root):
        """
        Runtime: 20 ms, faster than 95.87% of Python online submissions for Flatten Binary Tree to Linked List.
        Memory Usage: 13.8 MB, less than 24.04% of Python online submissions for Flatten Binary Tree to Linked List.

        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.inner_flatten(root)

    def inner_flatten(self,root):
        """
        :param root:
        :param pre_node:
        :return: flatten tree head node and tail node
        """
        if(None == root): return (root, root)
        elif(None == root.left and None == root.right):return (root, root)
        elif(None != root.left and None == root.right):
            (left_head, left_tail) = self.inner_flatten(root.left)
            root.right = left_head
            root.left = None
            return (root, left_tail)
        elif(None == root.left and None != root.right):
            (right_head, right_tail) = self.inner_flatten(root.right)
            root.right = right_head
            return (root, right_tail)
        else:
            (left_head, left_tail) = self.inner_flatten(root.left)
            (right_head, right_tail) = self.inner_flatten(root.right)
            left_tail.right = right_head
            root.left = None
            root.right = left_head
            return (root, right_tail)



    def self_testing(self):
        root = initFullBinaryTree("[1,2,5,3,4,null,6]")
        middle_print(root)
        pre_print(root)
        self.flatten(root)
        middle_print(root)

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
