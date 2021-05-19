# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/19. 

from suanec.slcs.utils.list_utils import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    142. Linked List Cycle II
    Medium

    4193

    313

    Add to List

    Share
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Notice that you should not modify the linked list.



    Example 1:


    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    Example 2:


    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    Example 3:


    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.


    Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.


    Follow up: Can you solve it using O(1) (i.e. constant) memory?
    """
    def detectCycle(self, head):
        """
        Runtime: 44 ms, faster than 52.02% of Python online submissions for Linked List Cycle II.
        Memory Usage: 19.8 MB, less than 40.34% of Python online submissions for Linked List Cycle II.

        Runtime: 48 ms, faster than 26.85% of Python online submissions for Linked List Cycle II.
        Memory Usage: 19.6 MB, less than 82.47% of Python online submissions for Linked List Cycle II.
        :type head: ListNode
        :rtype: ListNode
        """
        if(None == head):
            return None
        if(None == head.next):
            return None
        if(None == head.next.next):
            return None

        pre_header = ListNode(-1)
        pre_header.next = head
        fast = pre_header
        slow = pre_header
        fast = fast.next.next
        slow = slow.next
        while(fast != slow):
            if(None == fast.next):
                return None
            if(None == fast.next.next):
                return None
            fast = fast.next.next
            slow = slow.next

        enter = pre_header
        while(enter != slow):
            enter = enter.next
            slow = slow.next
        return enter

    def self_testing(self):
        l = initList([3,2,0,-4])
        l.next.next.next.next = l.next
        print(self.detectCycle(l))
        l = initList([1,2])
        l.next.next = l
        print(self.detectCycle(l))
        l = initList([-1])
        print(self.detectCycle(l))

Solution().self_testing()