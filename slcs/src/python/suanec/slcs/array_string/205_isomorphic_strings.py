# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/7/12. 

class Solution(object):
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



    Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Example 2:

    Input: s = "foo", t = "bar"
    Output: false
    Example 3:

    Input: s = "paper", t = "title"
    Output: true


    Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
    """
    def isIsomorphic(self, s, t):
        """
        Runtime: 28 ms, faster than 84.47% of Python online submissions for Isomorphic Strings.
        Memory Usage: 13.8 MB, less than 95.31% of Python online submissions for Isomorphic Strings.

        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        char_memo = {}
        value_key_memo = {}
        for i in range(len(t)):
            if(s[i] in char_memo):
                if(char_memo[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in value_key_memo):
                    return False
                else:
                    value_key_memo[t[i]] = [s[i]]
                char_memo[s[i]] = t[i]
        return True