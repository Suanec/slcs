# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/23. 

from suanec.slcs.utils.list_utils import *
from suanec.slcs.utils.tree_utils import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    109. Convert Sorted List to Binary Search Tree
    Medium

    2382

    90

    Add to List

    Share
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



    Example 1:


    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

    Example 2:

    Input: head = []
    Output: []

    Example 3:

    Input: head = [0]
    Output: [0]

    Example 4:

    Input: head = [1,3]
    Output: [3,1]


    Constraints:

    The number of nodes in head is in the range [0, 2 * 104].
    -10^5 <= Node.val <= 10^5
    '''
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

    def sortedListToBST_by_list(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        Runtime: 132 ms, faster than 47.94% of Python online submissions for Convert Sorted List to Binary Search Tree.
        Memory Usage: 25.5 MB, less than 21.90% of Python online submissions for Convert Sorted List to Binary Search Tree.
        """
        head_arr = []
        cur_point = head
        while(cur_point):
            head_arr.append(cur_point.val)
            cur_point = cur_point.next
        return self.sortedArrayToBST(head_arr)

    def sortedListToBST(self, head):
        if(None == head):
            return None
        cur_point = head
        head_count = 0
        while(cur_point):
            head_count += 1
            cur_point = cur_point.next
        self.cur_point = head
        return self.inner_sorted_list_to_bst(1, head_count)

    def inner_sorted_list_to_bst(self, start_idx, end_idx):
        '''
        inorder Traversal to fill all elements in list in a new tree construct by recursive.
        how to understand this solution：
        1. we count all elements in list so that we can know the tree constructure which corresponds the conditions of BST
        2. inorder traversal the specified BST
        3. fill the elements in list into the target tree.
        this is mean we traversal the tree by inorder function, fill the sorted elements at specified positions.
        Runtime: 124 ms, faster than 80.95% of Python online submissions for Convert Sorted List to Binary Search Tree.
        Memory Usage: 25.7 MB, less than 21.90% of Python online submissions for Convert Sorted List to Binary Search Tree.
        :param start_idx:
        :param end_idx:
        :return:
        '''
        if(start_idx > end_idx):
            return None
        mid_idx = start_idx + (end_idx - start_idx)/2
        left = self.inner_sorted_list_to_bst(start_idx, mid_idx -1)
        root = TreeNode(self.cur_point.val)
        root.left = left
        self.cur_point = self.cur_point.next
        root.right = self.inner_sorted_list_to_bst(mid_idx +1 , end_idx)
        return root


    def self_testing(self):
        level_print(self.sortedListToBST(initList([])))
        level_print(self.sortedListToBST(initList([0])))
        level_print(self.sortedListToBST(initList([1,3])))
        level_print(self.sortedListToBST(initList([-10,-3,0,5,9])))

if __name__ == '__main__':
    Solution().self_testing()

