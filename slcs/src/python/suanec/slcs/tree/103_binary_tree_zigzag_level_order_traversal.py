# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/18. 

from suanec.slcs.utils.tree_utils import *


class Solution(object):
    '''
    103. Binary Tree Zigzag Level Order Traversal
    Medium

    2351

    103

    Add to List

    Share
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
    '''
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(None == root): return []
        q = queue()
        # (node, left to right order flag)
        root_order = True
        q.push((root, root_order))
        res = []
        last_cur_order = not root_order
        last_seq = []
        while(not q.empty()):
            cur, cur_order = q.get()
            if(None != cur.left):
                q.push((cur.left, not cur_order))
            if(None != cur.right):
                q.push((cur.right, not cur_order))

            if(cur_order == last_cur_order or len(last_seq) == 0):
                last_seq.append(cur.val)
                last_cur_order = cur_order
            elif(cur_order != last_cur_order):
                if(last_cur_order):
                    res.append(last_seq)
                elif(not last_cur_order):
                    res.append(list(reversed(last_seq)))
                last_seq = []
                last_seq.append(cur.val)
                last_cur_order = cur_order
        if(len(last_seq) > 0):
            if(last_cur_order):
                res.append(last_seq)
            elif(not last_cur_order):
                res.append(list(reversed(last_seq)))

        return res

    def self_testing(self):
        """

        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        :return:
        """
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        print(self.zigzagLevelOrder(root=root))
        root = None
        print(self.zigzagLevelOrder(root=root))
        root = TreeNode(3)
        print(self.zigzagLevelOrder(root=root))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
