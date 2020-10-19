# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/19. 
from suanec.slcs.utils.list_utils import *

class Solution(object):
    '''
    21. Merge Two Sorted Lists
    Easy

    5153

    646

    Add to List

    Share
    Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.



    Example 1:


    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Example 2:

    Input: l1 = [], l2 = []
    Output: []
    Example 3:

    Input: l1 = [], l2 = [0]
    Output: [0]


    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
    '''
    def mergeTwoLists(self, l1, l2):
        """
        Runtime: 20 ms, faster than 93.93% of Python online submissions for Merge Two Sorted Lists.
        Memory Usage: 13.4 MB, less than 18.07% of Python online submissions for Merge Two Sorted Lists.
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rst_list = None
        if(not (l1 or l2)):
            return rst_list
        elif(not l1):
            rst_list = l2
        elif(not l2):
            rst_list = l1
        else:
            lp1 = l1
            lp2 = l2
            if(lp1.val < lp2.val):
                rst_list = lp1
                lp1 = lp1.next
            else:
                rst_list = lp2
                lp2 = lp2.next
            rst_tail = rst_list
            rst_tail.next = None

            while(lp1 and lp2):
                if(lp1.val < lp2.val):
                    rst_tail.next = lp1
                    lp1 = lp1.next
                else:
                    rst_tail.next = lp2
                    lp2 = lp2.next
                rst_tail = rst_tail.next
                rst_tail.next = None
            if(lp1):
                rst_tail.next = lp1
            elif(lp2):
                rst_tail.next = lp2
        return rst_list
    def self_testing(self):
        '''
        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        :return:
        '''
        printList(self.mergeTwoLists(initList([1,2,4]), initList([1,3,4])))
        printList(self.mergeTwoLists(initList([]), initList([])))
        printList(self.mergeTwoLists(initList([]), initList([0])))
        printList(self.mergeTwoLists(initList([1,1,2,4,1991]), initList([1,2,91])))


if __name__ == '__main__':
    Solution().self_testing()