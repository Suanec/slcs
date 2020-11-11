# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/11/11. 

class Solution(object):
    """
    709. To Lower Case
    Easy

    565

    1700

    Add to List

    Share
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



    Example 1:

    Input: "Hello"
    Output: "hello"
    Example 2:

    Input: "here"
    Output: "here"
    Example 3:

    Input: "LOVELY"
    Output: "lovely"
    Accepted
    234,459
    Submissions
    293,912
    """
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        Runtime: 12 ms, faster than 93.45% of Python online submissions for To Lower Case.
        Memory Usage: 13.6 MB, less than 30.83% of Python online submissions for To Lower Case.
        """
        return str.lower()
