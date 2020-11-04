# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/27. 
from suanec.slcs.utils.tree_utils import *


class Solution(object):
    """
    117. Populating Next Right Pointers in Each Node II
    Medium

    1841

    190

    Add to List

    Share
    Given a binary tree

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node,
    the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.



    Follow up:

    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


    Example 1:



    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A),
    your function should populate each next pointer to point to its next right node, just like in Figure B.
    The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


    Constraints:

    The number of nodes in the given tree is less than 6000.
    -100 <= node.val <= 100
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        Runtime: 40 ms, faster than 65.00% of Python online submissions for Populating Next Right Pointers in Each Node II.
        Memory Usage: 15.7 MB, less than 63.09% of Python online submissions for Populating Next Right Pointers in Each Node II.
        """
        if(None == root):
            return root
        # if(all([root.left, root.right])):
        #     root.left.next = root.right
        # else:
        #     return root
        cur_node = root
        if(root.left):
            head = pre = root.left
        else:
            head = pre = root.right
        while(head):
            while(cur_node.next):
                if(cur_node.left and cur_node.left != pre):
                    pre.next = cur_node.left
                    pre = pre.next
                if(cur_node.right and cur_node.right != pre):
                    pre.next = cur_node.right
                    pre = pre.next
                cur_node = cur_node.next
            if(cur_node.left and cur_node.left != pre):
                pre.next = cur_node.left
                pre = pre.next
            if(cur_node.right and cur_node.right != pre):
                pre.next = cur_node.right
                pre = pre.next
            cur_node = head
            while(cur_node and not any([cur_node.left,cur_node.right])):
                cur_node = cur_node.next
            if(cur_node):
                head = cur_node.left if(cur_node.left) else cur_node.right
            else:
                head = cur_node
            pre = head

        return root

    def self_testing(self):
        # self.connect_level_traversal(initFullBinaryTree("[1,2,3,4,5,null,7]"))
        self.connect(initFullBinaryTree("[1,null,-9,null,8,4,-3,null,null,-3,null,-6,null,null,-6,-4,-9,null,null,6]"))
        """
        Input
        [1,null,-9,null,8,4,-3,null,null,-3,null,-6,null,null,-6,-4,-9,null,null,6]
        Output
        [1,#,-9,#,8,#,4,#]
        Expected
        [1,#,-9,#,8,#,4,-3,#,-3,#,-6,#,-6,#,-4,-9,#,6,#]
        """

        self.connect(initFullBinaryTree("[1,2,3,4,5,null,6,7]"))
        self.connect(initFullBinaryTree("[1,2,3,4,5,null,7]"))
        """
        Your input
        [1,2,3,4,5,null,7]
        Output
        [1,#,2,3,#,4,5,#]
        Expected
        [1,#,2,3,#,4,5,7,#]
        """
        """
        Input
        [1,2,3,4,null,null,5]
        Output
        [1,#,2,3,#,4,#]
        Expected
        [1,#,2,3,#,4,5,#]
        """
        self.connect(initFullBinaryTree("[1,2,3,4,null,null,5]"))
        self.connect(initFullBinaryTree("[1,2,3,4,null,null,5,null,null,null,6]"))
        """
        [0,0,0,0,null,null,0,null,null,null,0]
        """

Solution().self_testing()