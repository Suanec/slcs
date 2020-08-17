# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.


# PreOrderLoop(TreeNode *root)
class Solution(object):
    # void PreOrderLoop(TreeNode *root)
    # {
    #     std::stack<TreeNode *> s;
    # TreeNode *cur, *top;
    # cur = root;
    # while (cur != NULL || !s.empty())
    # {
    # while (cur != NULL)
    #     {
    #         printf("%c ", cur->data);
    #     s.push(cur);
    #     cur = cur->left;
    #     }
    #
    #     top = s.top();
    #     s.pop();
    #
    #     cur = top->right;
    # }
    # }
    def PreOrderLoop(self, root):
        s = stack()
        cur = root
        top = None
        rst = []
        while(cur != None or not s.empty()):
            while(cur != None):
                rst.append(cur.val)
                s.push(cur)
                cur = cur.left
            # top = s.pick()
            # s.pop()
            top = s.pop()
            cur = top.right
        return rst

    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        print self.PreOrderLoop(root=root)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        print self.PreOrderLoop(root=root)
# Solution().self_testing()
