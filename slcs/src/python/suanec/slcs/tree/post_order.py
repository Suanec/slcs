# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.



class Solution(object):
    # # PostOrderLoop
    # void PostOrderLoop(TreeNode *root)
    # {
    #     std::stack<TreeNode *> s;
    # TreeNode *cur, *top, *last = NULL;
    # cur = root;
    # while (cur != NULL || !s.empty())
    # {
    # while (cur != NULL)
    #     {
    #         s.push(cur);
    #     cur = cur->left;
    #     }
    #
    #     top = s.top();
    #
    #     if (top->right == NULL || top->right == last){
    #     s.pop();
    #     printf("%c ", top->data);
    #     last = top;
    #     }
    #     else {
    #     cur = top->right;
    #     }
    # }
    # }
    def PostOrderLoop(self, root):
        s = stack()
        cur = top = last = None
        cur = root
        rst = []
        while(cur != None or not s.empty()):
            while(cur != None):
                s.push(cur)
                cur = cur.left

            top = s.pick()
            if(top.right == None or top.right == last):
                s.pop()
                rst.append(top.val)
                last = top
            else:
                cur = top.right
        return rst
    def self_testing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        print self.PostOrderLoop(root=root)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        print self.PostOrderLoop(root=root)

# Solution().self_testing()
