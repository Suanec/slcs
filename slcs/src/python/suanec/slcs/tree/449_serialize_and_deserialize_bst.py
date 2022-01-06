# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/20. 

from suanec.slcs.utils.tree_utils import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

class Codec:
    '''
    449. Serialize and Deserialize BST
    Medium

    1655

    88

    Add to List

    Share
    Serialization is converting a data structure or object into a sequence of bits
    so that it can be stored in a file or memory buffer,
    or transmitted across a network connection link to be
    reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree.
    There is no restriction on how your serialization/deserialization algorithm should work.
    You need to ensure that a binary search tree can be serialized to a string,
    and this string can be deserialized to the original tree structure.

    The encoded string should be as compact as possible.



    Example 1:

    Input: root = [2,1,3]
    Output: [2,1,3]
    Example 2:

    Input: root = []
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The input tree is guaranteed to be a binary search tree.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        Runtime: 116 ms, faster than 13.02% of Python online submissions for Serialize and Deserialize BST.
        Memory Usage: 34.6 MB, less than 5.95% of Python online submissions for Serialize and Deserialize BST.

        :type root: TreeNode
        :rtype: str
        """
        root_depth = self.tree_depth(root)
        if(None == root):return "[]"
        level_order_seq = self.level_order_list_full(root, root_depth)
        return str(level_order_seq)
        # print(middle_order_seq)

    def tree_depth(self, root):
        if(None == root):
            return 0
        depth = 1
        sub_depth = max(self.tree_depth(root.left), self.tree_depth(root.right))
        return sub_depth + 1

    def level_order_list_full(self, root, tree_depth):
        res = []
        null_value = None
        if(tree_depth < 1):
            return res
        q = queue()

        q.push((root, tree_depth))
        while(not q.empty()):
            (cur,cur_depth) = q.get()
            cur_val = null_value if(null_value == cur) else cur.val
            res.append(cur_val)
            if(cur_depth > 1):
                if(null_value != cur):
                    cur_left = cur.left if(cur.left) else null_value
                    cur_right = cur.right if(cur.right) else null_value
                    q.push((cur_left, cur_depth -1))
                    q.push((cur_right, cur_depth-1))
                # else:
                #     q.push((null_value, cur_depth -1))
                #     q.push((null_value, cur_depth-1))
        while(None == res[-1]):
            res = res[:-1]
        return res



    def initFullBinaryTree(self, source ="[5,4,1,null,1,null,4,2,null,2,null]"):
        if(not source):
            return None
        _source = eval(source.replace("null", "None"))
        source_len = len(_source)
        if(source_len < 1):
            return None
        root = TreeNode(_source[0])
        if(source_len % 2 == 0):
            _source.append(None)
        q = queue()
        q.push(root)
        for i in range(1,source_len,2):
            cur_left_val = None if(_source[i] == None) else TreeNode(_source[i])
            cur_right_val = None if(_source[i + 1] == None) else TreeNode(_source[i + 1])
            cur = q.get()
            if(None != cur_left_val):
                q.push(cur_left_val)
            if(None != cur_right_val):
                q.push(cur_right_val)
            cur.left = cur_left_val
            cur.right = cur_right_val
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # data.replace("#","null")
        return self.initFullBinaryTree(data)


    def self_testing(self):
        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # tree = ser.serialize(root)
        # ans = deser.deserialize(tree)
        # return ans
        pre_print(self.initFullBinaryTree())
        print(self.serialize(self.initFullBinaryTree()))
        pre_print(self.deserialize( self.serialize(self.initFullBinaryTree()) ))
        pre_print(self.deserialize( self.serialize(self.initFullBinaryTree('[]')) ))

if __name__ == '__main__':
    Codec().self_testing()