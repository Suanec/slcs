# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/16. 


from suanec.slcs.utils.tree_utils import *

class Solution(object):
    """
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

    Example:

    Given the sorted array: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

          0
         / \
       -3   9
       /   /
     -10  5
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        Runtime: 52 ms, faster than 99.19% of Python online submissions for Convert Sorted Array to Binary Search Tree.
        Memory Usage: 17 MB, less than 35.16% of Python online submissions for Convert Sorted Array to Binary Search Tree.
        """
        nums_len = len(nums)
        if(nums_len == 0):
            return None
        if(nums_len == 1):
            return TreeNode(nums[0])
        mid = nums_len / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root

    def self_testing(self):
        level_print(self.sortedArrayToBST([-10,-3,0,5,9]))
        level_print(self.sortedArrayToBST([1,2,3,4,5,6,7]))
        level_print(self.sortedArrayToBST([1]))
        level_print(self.sortedArrayToBST([]))
        level_print(self.sortedArrayToBST([1,2]))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
