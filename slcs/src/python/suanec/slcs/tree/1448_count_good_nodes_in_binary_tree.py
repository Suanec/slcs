# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/19. 

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    '''
    1448. Count Good Nodes in Binary Tree
    Medium

    290

    15

    Add to List

    Share
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.



    Example 1:
            3
           /  \
          1   4
         /   /  \
        3   1   5


    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
    Example 2:
              3
             /
            3
           / \
          4  2

    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
    Example 3:

    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.


    Constraints:

    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
    '''
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(None == root): return len([])
        sub_max = root.val
        left_good_nodes = self.sub_good_nodes(root.left, sub_max)
        right_good_nodes = self.sub_good_nodes(root.right, sub_max)
        return len([root.val] + left_good_nodes + right_good_nodes)

    def sub_good_nodes(self, root, sub_max):
        if(None == root): return []
        res = []
        if(root.val >= sub_max):
            res.append(root.val)
        left_good_nodes = self.sub_good_nodes(root.left, max(sub_max, root.val))
        right_good_nodes = self.sub_good_nodes(root.right, max(sub_max, root.val))
        return res + left_good_nodes + right_good_nodes



    def self_testing(self):
        '''
                3
               /  \
              1   4
             /   /  \
            3   1   5
        :return:
        '''

        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        print(self.goodNodes(root=root))
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        print(self.goodNodes(root=root))
        root = None
        print(self.goodNodes(root=root))
        root = TreeNode(3)
        print(self.goodNodes(root=root))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
