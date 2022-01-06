# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/11/5. 

class Solution(object):
    """
    14. Longest Common Prefix
    Easy

    3217

    2012

    Add to List

    Share
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".



    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.


    Constraints:

    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Runtime: 20 ms, faster than 80.35% of Python online submissions for Longest Common Prefix.
        Memory Usage: 13.7 MB, less than 72.78% of Python online submissions for Longest Common Prefix.
        """
        prefix_count = 0
        common_prefix = ""
        if(len(strs) < 1):
            return common_prefix
        min_length = min([len(input_str) for input_str in strs])
        for i in range(0,min_length):
            char_set = set()
            [char_set.add(input_str[i]) for input_str in strs]
            if(len(char_set) == 1):
                prefix_count += 1
                common_prefix += char_set.pop()
            elif(len(char_set) > 1):
                break
        return common_prefix

    def self_testing(self):
        print(self.longestCommonPrefix(["flower","flow","flight"]))
        print(self.longestCommonPrefix(["dog","racecar","car"]))

Solution().self_testing()
