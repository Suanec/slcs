# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17. 

from suanec.slcs.utils.tree_utils import *

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
class NAryTreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
