# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.


class Solution(object):
    # void LevelOrder(TreeNode *root)
    # {
    #     std::queue<TreeNode *> q;
    # TreeNode *front;
    #
    # if (root == NULL)return;
    #
    # q.push(root);
    #
    # while (!q.empty())
    # {
    #     front = q.front();
    # q.pop();
    #
    # if (front->left)
    # q.push(front->left);
    #
    # if (front->right)
    # q.push(front->right);
    #
    # printf("%c ", front->data);
    # }
    # }
    def LevelOrder(self, root):
        q = queue()
        front = None
        rst = []
        if(root == None): return rst
        q.push(root)
        while(not q.empty()):
            front = q.pop()
            if(front.left != None):
                q.push(front.left)
            if(front.right != None):
                q.push(front.right)
            rst.append(front.val)
        return rst

    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        print self.LevelOrder(root=root)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        print self.LevelOrder(root=root)

# Solution().self_testing()

