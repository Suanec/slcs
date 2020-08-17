# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.tree_utils import *

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = queue()
        q.push((root,0))
        stash = []
        while(not q.empty()):
            (cur_node, cur_node_level) = q.pop()
            if(cur_node):
                q.push((cur_node.left, cur_node_level +1))
                q.push((cur_node.right, cur_node_level +1))
                if(len(stash) > cur_node_level):
                    (pre_node_list, pre_node_count) = stash[cur_node_level]
                    pre_node_list.append(cur_node.val)
                    pre_node_count += 1
                    stash[cur_node_level] = (pre_node_list, pre_node_count)
                else:
                    pre_node_list = cur_node.val
                    pre_node_count = 1
                    stash.append(([pre_node_list], pre_node_count))
        rst = [pre_node_list for (pre_node_list, pre_node_count) in stash]
        rst.reverse()
        return rst

    def self_testing(self):
        '''
        Input:
            3
           / \
          9  20
            /  \
           15   7
        Output: [[3],[9,20],[15,7]]
        :return:
        '''

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.levelOrderBottom(root)

Solution().self_testing()

