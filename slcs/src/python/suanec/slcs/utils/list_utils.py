# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

# #############     List     # #############
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(source = []):
    if(len(source) == 0 ): return None
    if(len(source) == 1 ): return ListNode(source[0])
    head = ListNode(source[0])
    p = head
    for i in range(1,len(source)):
        p.next = ListNode(source[i])
        p = p.next
    return head

def printList(head):
    p = head
    while(p != None):
        print(p.val)
        p = p.next
    print('\n-\n')