# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.


class Solution(object):
    # # InOrderLoop(TreeNode *root)
    # void InOrderLoop(TreeNode *root)
    # {
    #     std::stack<TreeNode *> s;
    # TreeNode *cur;
    # cur = root;
    # while (cur != NULL || !s.empty())
    # {
    # while (cur != NULL)
    #     {
    #         s.push(cur);
    #     cur = cur->left;
    #     }
    #
    #     cur = s.top();
    #     s.pop();
    #     printf("%c ", cur->data);
    #
    #     cur = cur->right;
    # }
    # }
    def InOrderLoop(self, root):
        s = stack()
        cur = root
        rst = []
        while(cur != None or not s.empty()):
            while(cur != None):
                s.push(cur)
                cur = cur.left
            cur = s.pop()
            rst.append(cur.val)

            cur = cur.right
        return rst

    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        print self.InOrderLoop(root=root)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        print self.InOrderLoop(root=root)


Solution().self_testing()

