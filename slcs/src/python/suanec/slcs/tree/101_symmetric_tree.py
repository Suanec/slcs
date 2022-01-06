# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/19. 

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    '''
    101. Symmetric Tree
    Easy

    4410

    107

    Add to List

    Share
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3


    But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3


    Follow up: Solve it both recursively and iteratively.
    '''
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetricRecursively(root)
        # return self.isSymmetricIteratively(root)

    def isSymmetricIteratively(self, root):
        pass

    def isSymmetricRecursively(self, root):
    # def isSymmetricRecursively1(self, root):
        '''
        Runtime: 24 ms, faster than 72.95% of Python online submissions for Symmetric Tree.
        Memory Usage: 13.1 MB, less than 24.60% of Python online submissions for Symmetric Tree.
        :param root:
        :return:
        '''
        if(None == root):return True
        return self.tree_symmetric(root.left, root.right)


    def tree_symmetric(self, left_root, right_root):
        if(None == left_root and None == right_root):
            return True
        elif(None == left_root or None == right_root):
            return False
        else:
            if(left_root.val != right_root.val):
                return False
            else:
                return self.tree_symmetric(left_root.left, right_root.right) and self.tree_symmetric(
                    left_root.right, right_root.left
                )

    def pre_order_list(self, root):
        res = []
        if(None == root): return []
        res.append(root.val)
        res += self.middle_order_list(root.left)
        res += self.middle_order_list(root.right)
        return res

    def middle_order_list(self, root):
        res = []
        if(None == root): return []
        res += self.middle_order_list(root.left)
        res.append(root.val)
        res += self.middle_order_list(root.right)
        return res

    def middle_order_list_reverse(self, root):
        res = []
        if(None == root): return []
        res += self.middle_order_list_reverse(root.right)
        res.append(root.val)
        res += self.middle_order_list_reverse(root.left)
        return res

    # def isSymmetricRecursively(self, root):
    def isSymmetricRecursively_time_limit_exceeded(self, root):
        root_depth = self.tree_depth(root)
        if(None == root):return True
        middle_order_seq = self.middle_order_list_full(root, root_depth)
        # print(middle_order_seq)
        middle_order_seq_reverse = list(reversed(middle_order_seq))
        is_symmetric_list = [
            x for (x,y) in zip(middle_order_seq, middle_order_seq_reverse) if (x != y)
        ]
        return 0 == len(is_symmetric_list)

    def tree_depth(self, root):
        if(None == root):
            return 0
        depth = 1
        sub_depth = max(self.tree_depth(root.left), self.tree_depth(root.right))
        return sub_depth + 1

    def middle_order_list_full(self, root, tree_depth):
        res = []
        null_value = "suanec"
        if(tree_depth < 1):
            return res
        if(None == root):
            res = self.middle_order_list_full(None, tree_depth - 1)
            res.append(None)
            res += self.middle_order_list_full(None, tree_depth - 1)
        else:
            res = self.middle_order_list_full(root.left, tree_depth - 1)
            res.append(root.val)
            res += self.middle_order_list_full(root.right, tree_depth - 1)
        return res



    def self_testing(self):
        '''
        True
        False
        True
        False
        False
        False
        :return:
        '''

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        print(self.isSymmetric(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        print(self.isSymmetric(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        print(self.isSymmetric(root))
        '''
        [1,2,2,2,null,2]
        '''
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(2)
        root.right.left = TreeNode(2)
        print(self.isSymmetric(root))
        '''
                      5
                 /         \
                4           1
              /   \       /   \
             n     1     n     4 
            / \   / \   / \   / \
           n   n  2  n  n  n  2  n
        '''
        root = initFullBinaryTree("[5,4,1,null,1,null,4,2,null,2,null]")
        print(self.isSymmetric(root))
        root = initFullBinaryTree(" [ 9,96,96,94,58,58,94,null,-75,-89,null,null,-89,-75,null,null,79,-57,null,null,-57,79,null,null,-90,-54,null,null,-54,-90,null,null,86,-76,89,89,-76,86,null,-5,null,76,null,1,null,null,1,null,76,null,-5,-39,null,null,79,24,null,null,24,79,null,null,-39,null,76,95,32,91,null,null,91,32,95,76,null,null,-56,39,-36,31,23,82,null,null,82,23,31,-36,39,-56,null,null,-77,88,null,-16,-29,null,-87,null,-77,66,-73,-73,66,-77,null,-87,null,-29,-16,null,88,null,-77,null,-46,88,null,-39,48,-46,null,-84,74,-78,null,-49,null,78,-80,-80,78,null,-49,null,-78,74,-84,null,-46,48,-39,null,88,-46,null,null,77,34,-83,null,33,-51,null,-43,18,null,7,-12,39,27,null,-76,60,-73,null,63,null,null,63,null,-73,60,-76,null,27,39,-12,7,null,18,-43,null,-51,33,null,-83,34,null,77,62,null,null,72,null,-6,null,40,2,null,null,-18,-38,null,-76,null,-45,null,69,null,83,null,null,31,86,null,null,7,null,-43,-43,null,7,null,null,86,31,null,null,83,null,69,null,-45,null,-76,-38,null,-18,null,null,2,40,null,-6,null,72,null,null,62,null,77,null,76,15,null,1,null,null,43,90,null,-36,null,61,null,97,96,null,51,74,50,null,91,null,-48,null,84,-39,null,null,-39,84,null,-48,null,91,null,50,74,51,null,96,97,null,61,null,-36,null,90,43,null,null,1,null,15,76,null,77,null,null,-7,-23,49,-8,null,45,null,73,86,null,-14,-97,null,-74,null,-20,55,23,null,null,84,-79,null,25,91,37,null,null,-83,-38,null,null,-31,-31,null,null,-38,-83,null,null,37,91,25,null,-79,84,null,null,23,55,-20,null,-74,null,-97,-14,null,86,73,45,null,null,-8,49,-23,-7,null,null,89,null,-16,null,-63,null,-81,1,-23,null,-72,null,-59,-6,null,null,-12,-34,64,19,null,null,-93,null,8,null,39,-95,null,24,90,46,null,-71,null,75,10,null,65,-72,null,null,-72,65,null,10,75,null,-71,null,46,90,24,null,-95,39,null,8,null,-93,null,null,19,64,-34,-12,null,null,-6,-59,null,-72,null,-23,1,-81,null,-63,null,-16,null,89,null,-58,null,35,-57,72,null,null,44,-47,null,null,-90,-75,null,null,9,88,null,26,null,null,-49,null,73,null,30,null,-64,62,null,null,31,39,79,-92,null,-89,null,41,null,-63,94,null,65,null,16,-76,null,-57,-28,-28,-57,null,-76,16,null,65,null,94,-63,null,41,null,-89,null,-92,79,39,31,null,null,62,-64,null,30,null,73,null,-49,null,null,26,null,88,9,null,null,-75,-90,null,null,81,44,null,null,72,-57,35,null,-58,null,6,75,null,-56,null,80,-58,-10,null,null,63,null,2,-14,null,null,-55,null,-71,68,-34,null,1,-14,null,null,64,56,-41,10,null,34,null,-8,null,-40,-98,null,-10,null,-91,-40,null,-89,2,53,null,null,-13,8,null,null,83,75,-27,82,null,null,82,-27,75,null,83,null,8,-13,null,null,53,2,-89,null,-40,-91,null,-10,null,-98,-40,null,-8,null,34,null,10,-41,56,64,null,null,-14,1,null,-34,68,-71,null,-55,null,null,-14,2,null,63,null,null,-10,-58,80,null,-56,null,75,6,null,null,-73,68,null,null,94,-42,null,null,26,38,63,79,-36,null,-97,null,18,14,null,null,-82,null,64,77,-60,null,-31,null,88,65,null,-51,null,null,-87,null,60,86,null,-31,null,null,-33,-24,null,null,-18,91,null,-9,-41,32,null,-53,null,null,-87,-68,null,null,-71,30,-52,-60,null,null,26,-78,82,82,-78,26,null,null,-60,-52,30,-71,null,null,-68,-87,null,null,-53,null,32,-41,-9,null,91,-18,null,null,-24,-33,null,null,-31,null,86,60,null,-87,null,null,-51,null,65,88,null,-31,null,-60,77,64,null,-82,null,null,14,18,null,-97,null,-36,79,63,38,26,null,null,-42,94,null,null,68,-73] ")
        print(self.isSymmetric(root))

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
