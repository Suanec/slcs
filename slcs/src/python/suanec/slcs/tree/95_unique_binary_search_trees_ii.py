# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/18.

from suanec.slcs.utils.tree_utils import *

# https://leetcode.com/problems/unique-binary-search-trees-ii/

class Solution(object):
    '''
    Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

    Example:

    Input: 3
    Output:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    Explanation:
    The above output corresponds to the 5 unique BST's shown below:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


    Constraints:

    0 <= n <= 8
    '''
    def generateTrees(self, n):
        """
        Runtime: 52 ms, faster than 74.15% of Python online submissions for Unique Binary Search Trees II.
        Memory Usage: 15.9 MB, less than 64.35% of Python online submissions for Unique Binary Search Trees II.
        :type n: int
        :rtype: List[TreeNode]
        """
        node_list = range(1,n+1)
        res = self.sub_generate_tree(node_list)
        return res


    def sub_generate_tree(self, value_list):
        n = len(value_list)
        if(n == 0): return []
        if(n == 1): return [TreeNode(value_list[0])]
        if(n == 2): return self.sub_generate_tree_2(value_list)
        if(n == 3): return self.sub_generate_tree_3(value_list)
        res = []
        for i in xrange(0,n):
            left_part = value_list[:i]
            right_part = value_list[i+1:]
            left_tree_list = self.sub_generate_tree(left_part)
            right_tree_list = self.sub_generate_tree(right_part)
            if(len(left_tree_list) < 1):
                for right_tree in right_tree_list:
                    cur_root = TreeNode(value_list[i])
                    cur_root.right = right_tree
                    res.append(cur_root)
            elif(len(right_tree_list) < 1):
                for left_tree in left_tree_list:
                    cur_root = TreeNode(value_list[i])
                    cur_root.left = left_tree
                    res.append(cur_root)
            else:
                for left_tree in left_tree_list:
                    for right_tree in right_tree_list:
                        cur_root = TreeNode(value_list[i])
                        cur_root.left = left_tree
                        cur_root.right = right_tree
                        res.append(cur_root)
        return res

    def insert_root_node(self, root_node_value, sub_tree, is_left):
        root_node = TreeNode(root_node_value)
        if(is_left):
            root_node.left = sub_tree
        else:
            root_node.right = sub_tree
        return root_node

    def sub_generate_tree_2(self, value_list):
        res = []
        sorted_value_list = sorted(value_list)
        if(len(value_list) == 2):
            root = TreeNode(sorted_value_list[0])
            root.right = TreeNode(sorted_value_list[1])
            res.append(root)
            root = TreeNode(sorted_value_list[1])
            root.left = TreeNode(sorted_value_list[0])
            res.append(root)
        return res

    def sub_generate_tree_3(self, value_list):
        res = []
        sorted_value_list = sorted(value_list)
        if(len(value_list) == 3):
            sub_2 = self.sub_generate_tree_2(sorted_value_list[1:])
            res.append(self.insert_root_node(sorted_value_list[0], sub_2[0], False))
            res.append(self.insert_root_node(sorted_value_list[0], sub_2[1], False))
            root = TreeNode(sorted_value_list[1])
            root.left = TreeNode(sorted_value_list[0])
            root.right = TreeNode(sorted_value_list[2])
            res.append(root)
            sub_2 = self.sub_generate_tree_2(sorted_value_list[:-1])
            res.append(self.insert_root_node(sorted_value_list[2], sub_2[0], True))
            res.append(self.insert_root_node(sorted_value_list[2], sub_2[1], True))
        return res





    def self_testing(self):
        '''
        0，0
        1，1
        2，2
        3，2+1+2=5
        4，5+2+2+5=14
        5，14+5+2*2+5+14=42
        6，42+14+2*5+2*5+14+42=132
        7，132+42+2*14+5*5+2*14+42+132=429
        8，429+132+2*42+5*14+14*5+42*2+132+429=1430
        :return:
        '''
        print("---------")
        [level_print(root) for root in self.generateTrees(0)]
        print("---------")
        [level_print(root) for root in self.generateTrees(1)]
        print("---------")
        [level_print(root) for root in self.generateTrees(2)]
        print("---------")
        [level_print(root) for root in self.generateTrees(3)]
        print("---------")
        [level_print(root) for root in self.generateTrees(4)]
        print("---------")
        print(len(self.generateTrees(5)))
        print("---------")
        print(len(self.generateTrees(6)))
        print("---------")
        print(len(self.generateTrees(7)))
        print("---------")
        print(len(self.generateTrees(8)))
        pass

if __name__ == '__main__':
    s = Solution()
    s.self_testing()

