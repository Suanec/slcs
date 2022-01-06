# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/23.
from suanec.slcs.utils.tree_utils import *
from collections import deque

class queue(deque):
    def push(self, x):
        self.append(x)

    def pick(self, idx = 0):
        return self[idx] if(len(self) > idx) else None

    def empty(self):
        return len(self) == 0

    def pop(self):
        return self.popleft()

    def get(self):
        tmp = self[0]
        self.remove(tmp)
        return tmp

    def self_testing(self):
        q = queue()
        q.push(5);q.push(3);q.push(4);q.push(51)
        print(q)
        print(q.pick())
        print(q.pick(2))
        print(q.get())
        print(q)

class Solution(object):
    '''
    116. Populating Next Right Pointers in Each Node
    Medium

    2447

    148

    Add to List

    Share
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.



    Follow up:

    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


    Example 1:



    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


    Constraints:

    The number of nodes in the given tree is less than 4096.
    -1000 <= node.val <= 1000
    '''
    def connect_level_traversal(self, root):
        """
        :type root: Node
        :rtype: Node
        Runtime: 88 ms, faster than 8.97% of Python online submissions for Populating Next Right Pointers in Each Node.
        Memory Usage: 16.8 MB, less than 12.76% of Python online submissions for Populating Next Right Pointers in Each Node.
        """
        if(None == root):
            return root
        q = queue()
        # root.__dict__["next"] = None
        root.next = None
        q.push((root,0))
        while(not q.empty()):
            (cur_node,cur_level) = q.pop()
            if(cur_node):
                # cur_node.__dict__["next"] = None
                (next_node,next_level) = q.pick(0) if(not q.empty()) else (None, -1)
                if(cur_level == next_level):
                    cur_node.next = next_node
                else:
                    cur_node.next = None
                q.push((cur_node.left, cur_level + 1))
                q.push((cur_node.right, cur_level + 1))

        return root
    def connect(self, root):
        """
        public class Solution {
            public void connect(TreeLinkNode root) {
                TreeLinkNode level_start=root;
                while(level_start!=null){
                    TreeLinkNode cur=level_start;
                    while(cur!=null){
                        if(cur.left!=null) cur.left.next=cur.right;
                        if(cur.right!=null && cur.next!=null) cur.right.next=cur.next.left;

                        cur=cur.next;
                    }
                    level_start=level_start.left;
                }
            }
        }
        Runtime: 48 ms, faster than 91.54% of Python online submissions for Populating Next Right Pointers in Each Node.
        Memory Usage: 16.7 MB, less than 13.18% of Python online submissions for Populating Next Right Pointers in Each Node.
        :param root:
        :return:
        """
        if(None == root):
            return root
        pre_node = root
        cur_node = pre_node.left
        if(not cur_node): return root
        cur_node.next = pre_node.right
        while(cur_node.left and pre_node.left.left):
            cur_node.left.next = cur_node.right
            cur_node.right.next = cur_node.next.left if(cur_node.next) else cur_node.next
            cur_node = cur_node.next
            if(not cur_node):
                cur_node = pre_node.left.left
                pre_node = pre_node.left
        return root


    def self_testing(self):
        self.connect(initFullBinaryTree("[0]"))
        self.connect(initFullBinaryTree("[1,2,3,4,5,6,7]"))
        self.connect(initFullBinaryTree("[1, 2,3, 4,5,6,7, 41,42,51,52,61,62,71,72]"))

if __name__ == '__main__':
    Solution().self_testing()
