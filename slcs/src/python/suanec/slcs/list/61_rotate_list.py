# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

from suanec.slcs.utils.list_utils import *
# https://leetcode-cn.com/problems/rotate-list/
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(k < 1) : return head
        if(head == None): return head
        if(head.next == None): return head
        count = 0
        cur_head = head
        cur_tail = head
        while(k > 0 and cur_tail.next != None):
            cur_tail = cur_tail.next
            count += 1
            k -= 1
        if(k > 0):
            k += count
            count += 1
            k %= count
            return self.rotateRight(head, k)
        else:
            # 1->2->3->    4->5->NULL
            # head  tail   tail_p/pre
            pre_head = head
            pre_tail = cur_head
            cur_head = cur_head.next
            while(cur_tail.next != None):
                pre_tail = cur_head
                cur_head = cur_head.next
                cur_tail = cur_tail.next
            cur_tail.next = pre_head
            pre_tail.next = None
            head = cur_head
            return head
    def self_testing(self):
        # 1->2->3->4->5->NULL, k = 2
        source = [1,2,3,4,5]
        head = initList(source)
        s = Solution()
        # printList(s.rotateRight(head, 2))
        source = [1,2,3,4,5]
        head = initList(source)
        # printList(s.rotateRight(head, 1))
        source = [1,2,3,4,5]
        head = initList(source)
        # printList(s.rotateRight(head, 3))
        # 0->1->2->NULL, k = 4
        source = [0,1,2]
        head = initList(source)
        s = Solution()
        # printList(s.rotateRight(head, 4))


        source = [0,1,2,3,4]
        head = initList(source)
        s = Solution()
        # printList(s.rotateRight(head, 8))

        source = [1]
        head = initList(source)
        s = Solution()
        # printList(s.rotateRight(head, 1))

        source = [1,2,3]
        head = initList(source)
        s = Solution()
        # printList(s.rotateRight(head, 2000000000))


        source = [1,2,3]
        head = initList(source)
        s = Solution()
        printList(s.rotateRight(head, 19))

if __name__ == '__main__':

    s = Solution()
    s.self_testing()
