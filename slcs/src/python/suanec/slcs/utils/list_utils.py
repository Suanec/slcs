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

def equalsList(head1, head2):
    '''
    print(equalsList(initList([]),initList([])))
    print(equalsList(initList([1]),initList([])))
    print(equalsList(initList([1]),initList([1,2])))
    print(equalsList(initList([2]),initList([1,2])))
    :param head1:
    :param head2:
    :return:
    '''
    # if(not head1 and not head2):return True
    # if(not head1): return False
    # if(not head2): return False
    p = head1; q = head2
    while(p and q):
        if(p.val != q.val):
            return False
        p = p.next
        q = q.next
    if(None != p or None != q):
        return False
    return True

def equalSeq(seq1, seq2):
    if(not seq1 and not seq2):
        return True
    if(not(seq1 and seq2)):
        return False
    if(len(seq1) != len(seq2)):
        return False
    result = True
    for part1,part2 in zip(seq1,seq2):
        if(isinstance(part1, list) and isinstance(part2, list)):
            result = result and equalSeq(part1,part2)
        elif(not isinstance(part1, list) and not isinstance(part2, list)):
            result = result and (part1 == part2)
        else: return False
        if(not result): return result
    return result

