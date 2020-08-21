# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/21. 

from suanec.slcs.utils.tree_utils import *

class Solution(object):
    '''
    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


    Constraints:

    1 <= n <= 19
    '''
    def numTrees(self, n):
        """
        0，0
        1，1
        2，2
        3，2+1+2=5
        4，5+2+2+5=14
        5，14+5+2*2+5+14=42
        6，42+14+2*5+2*5+14+42=132
        7，132+42+2*14+5*5+2*14+42+132=429
        8，429+132+2*42+5*14+14*5+42*2+132+429=1430
        :type n: int
        :rtype: int
        """
        dp_seq = [0] * (n+1)
        dp_seq[0] = 0
        if(n < 1): return dp_seq[-1]
        dp_seq[1] = 1
        if(n < 2): return dp_seq[-1]
        dp_seq[2] = 2
        if(n < 3): return dp_seq[-1]
        dp_seq[3] = 5
        if(n < 4): return dp_seq[-1]
        dp_seq[4] = 14
        if(n < 5): return dp_seq[-1]
        dp_seq[0] = 1
        for cur_max in xrange(5, n+1):
            for root_value in xrange(1, cur_max + 1):
                dp_seq[cur_max] += dp_seq[root_value -1] * dp_seq[cur_max - root_value]
        return dp_seq[n]

    def numTreesRecursively(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_seq = [0] * (n+1)
        dp_seq[0] = 0
        if(n < 1): return dp_seq[-1]
        dp_seq[1] = 1
        if(n < 2): return dp_seq[-1]
        for root_value in xrange(1, n + 1):
            left_part_sub = root_value - 1
            right_part_sub = n - root_value
            left_tree_count = self.numTrees(left_part_sub)
            left_tree_count = left_tree_count if(0 < left_tree_count) else 1
            right_tree_count = self.numTrees(right_part_sub)
            right_tree_count = right_tree_count if(0 < right_tree_count) else 1
            dp_seq[n] += left_tree_count * right_tree_count
        return dp_seq[-1]
        # if(n < 2): return dp_seq[-1]
        # for root_value in xrange(1, n + 1):
        #     left_part_sub = root_value - 1
        #     right_part_sub = n - root_value
        #     left_tree_count = dp_seq[left_part_sub] if(0 != dp_seq[left_part_sub]) else 1
        #     right_tree_count = dp_seq[right_part_sub] if(0 < dp_seq[right_part_sub]) else 1
        #     dp_seq[n] += left_tree_count * right_tree_count
        return dp_seq[-1]

    def self_testing(self):
        print(self.numTrees(0))
        print(self.numTrees(1))
        print(self.numTrees(2))
        print(self.numTrees(3))
        print(self.numTrees(4))
        print(self.numTrees(5))
        print(self.numTrees(6))
        print(self.numTrees(7))
        print(self.numTrees(8))
        print(self.numTrees(19))
        pass

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
