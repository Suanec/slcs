# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

from suanec.slcs.utils.tree_utils import *

# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
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
                    (pre_node_sum, pre_node_count) = stash[cur_node_level]
                    pre_node_sum += cur_node.val
                    pre_node_count += 1
                    stash[cur_node_level] = (pre_node_sum, pre_node_count)
                else:
                    pre_node_sum = cur_node.val
                    pre_node_count = 1
                    stash.append((pre_node_sum, pre_node_count))
        rst = [pre_node_sum * 1. / pre_node_count for (pre_node_sum, pre_node_count) in stash]
        return rst

    def self_testing(self):
        '''
        Input:
            3
           / \
          9  20
            /  \
           15   7
        Output: [3, 14.5, 11]
        Explanation:
        The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
        :return:
        '''

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        print(self.averageOfLevels(root))
