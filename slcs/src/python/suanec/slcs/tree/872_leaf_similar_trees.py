# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/4. 

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    """
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



    Example 1:


    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
    Example 2:

    Input: root1 = [1], root2 = [1]
    Output: true
    Example 3:

    Input: root1 = [1], root2 = [2]
    Output: false
    Example 4:

    Input: root1 = [1,2], root2 = [2,2]
    Output: true
    Example 5:


    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false


    Constraints:

    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
    """
    def leafSimilar(self, root1, root2):
        """
        Runtime: 24 ms, faster than 58.52% of Python online submissions for Leaf-Similar Trees.
        Memory Usage: 13 MB, less than 21.40% of Python online submissions for Leaf-Similar Trees.
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if(None == root1 and None == root2):
            return True
        elif(not (root1 and root2)):
            return False
        else:
            root1_seq = self.leaf_sequence(root1, [])
            root2_seq = self.leaf_sequence(root2, [])
            return len(root1_seq) == len(root2_seq) and 0 == len([(x,y) for (x,y) in zip(root1_seq, root2_seq) if(x != y)])

    def leaf_sequence(self, root, _last_seq):
        last_seq = _last_seq
        if(None == root):
            return last_seq
        if(None == root.left and None == root.right):
            last_seq.append(root.val)
        else:
            self.leaf_sequence(root.left, last_seq)
            self.leaf_sequence(root.right, last_seq)
        return last_seq


    def self_testing(self):
        root1 = initFullBinaryTree("[3,5,1,6,2,9,8,null,null,7,4]")
        root2 = initFullBinaryTree("[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]")
        assert True == self.leafSimilar(root1, root2)
        root1 = initFullBinaryTree("[1]")
        root2 = initFullBinaryTree("[1]")
        assert True == self.leafSimilar(root1, root2)
        root1 = initFullBinaryTree("[1]")
        root2 = initFullBinaryTree("[2]")
        assert False == self.leafSimilar(root1, root2)
        root1 = initFullBinaryTree("[1,2]")
        root2 = initFullBinaryTree("[2,2]")
        assert True == self.leafSimilar(root1, root2)
        root1 = initFullBinaryTree("[1,2,3]")
        root2 = initFullBinaryTree("[1,3,2]")
        assert False == self.leafSimilar(root1, root2)
        root1 = initFullBinaryTree("[3,5,1,6,2,9,8,null,null,7,4]")
        root2 = initFullBinaryTree("[3,5,1,6,7,4,2,null,null,null,null,null,null,9,11,null,null,8,10]")
        assert False == self.leafSimilar(root1, root2)

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
