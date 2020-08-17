# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from utils.list_utils import *
# https://leetcode-cn.com/problems/merge-k-sorted-lists/
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if(not list1 and not list2):
            return None
        if(not list1 and list2):
            return list2
        if(list1 and not list2):
            return list1
        left_cur = list1
        right_cur = list2
        new_head = None
        new_cur = None
        while(left_cur and right_cur):
            if(not new_head):
                if(left_cur.val < right_cur.val):
                    new_head = left_cur
                    left_cur = left_cur.next
                else:
                    new_head = right_cur
                    right_cur = right_cur.next
                new_cur = new_head
            else:
                if(left_cur.val < right_cur.val):
                    new_cur.next = left_cur
                    new_cur = new_cur.next
                    left_cur = left_cur.next
                else:
                    new_cur.next = right_cur
                    new_cur = new_cur.next
                    right_cur = right_cur.next

        if(left_cur):
            new_cur.next = left_cur
            return new_head
        if(right_cur):
            new_cur.next = right_cur
            return new_head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [x for x in lists if x]
        if(len(lists) < 1):
            return None
        if(len(lists) == 1):
            return lists[0]
        head = lists[0]
        for i in xrange(1,len(lists)):
            head = self.merge2Lists(head, lists[i])
        return head
    def self_testing(self):
        lists = [initList(x) for x in [[1,4,5],[1,3,4],[2,6]]]
        lists = [initList(x) for x in [[1]]]
        printList(self.mergeKLists(lists))

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
