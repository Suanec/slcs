# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.list_utils import *
from suanec.slcs.utils.time_utils import *
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

    def mergeKLists_list_by_list(self, lists):
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
            head = self.mergeTwoLists(head, lists[i])
        return head

    def mergeKLists_sorted(self, lists):
        lists = [x for x in lists if x]
        if(len(lists) < 1):
            return None
        if(len(lists) == 1):
            return lists[0]
        idx_list = [x for x in lists]
        idx_list.sort(key=lambda x : x.val)
        rst_head = idx_list[0]
        rst_cur = rst_head
        idx_list[0] = idx_list[0].next
        while(any(idx_list)):
            idx_list.sort(key=lambda x : x.val)
            rst_cur.next = idx_list[0]
            idx_list[0] = idx_list[0].next
            if(None == idx_list[0]):
                idx_list = idx_list[1:]
            rst_cur = rst_cur.next
        return rst_head

    def mergeKLists(self, lists):
        def find_min(_idx_list = []):
            if(None == _idx_list): return None, None
            if(0 == len(_idx_list)): return None, None
            rst_node = _idx_list[0]
            rst_idx = 0
            for (index, node) in enumerate(_idx_list):
                if(node.val <= rst_node.val):
                    rst_node = node
                    rst_idx = index
            return rst_node, rst_idx

        lists = [x for x in lists if x]
        if(len(lists) < 1):
            return None
        if(len(lists) == 1):
            return lists[0]
        idx_list = [x for x in lists]
        min_node, min_index = find_min(idx_list)
        rst_head = min_node
        rst_cur = rst_head
        idx_list[min_index] = idx_list[min_index].next
        while(any(idx_list)):
            min_node, min_index = find_min(idx_list)
            rst_cur.next = min_node
            idx_list[min_index] = idx_list[min_index].next
            if(None == idx_list[min_index]):
                idx_list.pop(min_index)
            rst_cur = rst_cur.next
        return rst_head


    def self_testing(self):
        print([0] * 8)
        print(sorted([1,4,9,2,3]))
        lists = [initList(x) for x in [[1,4,5],[1,3,4],[2,6]]]
        printList(self.mergeKLists(lists))
        def wrapper():
            lists = [initList(x) for x in [[1,4,5],[1,3,4],[2,6]]]
            self.mergeKLists(lists)

        print(time_calc(wrapper, 30))
        lists = [initList(x) for x in [[1]]]
        printList(self.mergeKLists(lists))
        print(time_calc(self.mergeKLists, 10, lists))

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
