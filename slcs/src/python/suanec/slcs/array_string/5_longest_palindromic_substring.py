# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/11/21. 
class Solution(object):
    """
    5. Longest Palindromic Substring
    Medium

    8687

    602

    Add to List

    Share
    Given a string s, return the longest palindromic substring in s.



    Example 1:

    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:

    Input: s = "cbbd"
    Output: "bb"
    Example 3:

    Input: s = "a"
    Output: "a"
    Example 4:

    Input: s = "ac"
    Output: "a"


    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case),

    """
    def longestPalindrome(self, s):
        """
        Runtime: 96 ms, faster than 97.25% of Python online submissions for Longest Palindromic Substring.
        Memory Usage: 13.6 MB, less than 70.01% of Python online submissions for Longest Palindromic Substring.
        :param s:
        :return:
        """
        len_s = len(s)
        if(len_s < 2):
            return s
        start = 0
        max_result = s[0]
        max_len = 1
        while(start < len_s -1):
            left = right = start
            while(right < len_s -1 and s[right + 1] == s[right]):
                right += 1
            start = right + 1
            while(right < len_s -1 and left > 0 and s[right + 1] == s[left -1]):
                right += 1
                left -= 1
            cur_len = right - left + 1
            if(max_len < cur_len):
                max_result = s[left:right+1]
                max_len = cur_len
        return max_result

    # def longestPalindrome(self, s):
    def longestPalindrome_existly(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 80 ms, faster than 98.01% of Python online submissions for Longest Palindromic Substring.
        Memory Usage: 13.5 MB, less than 86.16% of Python online submissions for Longest Palindromic Substring.
        class Solution {
            public:
                string longestPalindrome(string s) {
                    if (s.size() < 2)
                        return s;
                    int len = s.size(), max_left = 0, max_len = 1, left, right;
                    for (int start = 0; start < len && len - start > max_len / 2;) {
                        left = right = start;
                        while (right < len - 1 && s[right + 1] == s[right])
                            ++right;
                        start = right + 1;
                        while (right < len - 1 && left > 0 && s[right + 1] == s[left - 1]) {
                            ++right;
                            --left;
                        }
                        if (max_len < right - left + 1) {
                            max_left = left;
                            max_len = right - left + 1;
                        }
                    }
                    return s.substr(max_left, max_len);
                }
            };
        """
        len_s = len(s)
        if(len_s < 2):
            return s
        max_left = left = right = start = 0
        max_len = 1
        while(start < len_s and (len_s - start) > max_len / 2):
            left = right = start
            while(right < len_s -1 and s[right + 1] == s[right]):
                right += 1
            start = right + 1
            while(right < len_s -1 and left > 0 and s[right + 1] == s[left - 1]):
                right += 1
                left -= 1
            cur_len = right - left + 1
            if(max_len < cur_len):
                max_left = left
                max_len = cur_len
        return s[max_left : max_left + max_len]

    def self_testing(self):
        """
        bb
        bab
        a
        a
        :return:
        """
        print(self.longestPalindrome("cbbd"))
        print(self.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        print(self.longestPalindrome("babad"))
        print(self.longestPalindrome("a"))
        print(self.longestPalindrome("ac"))

Solution().self_testing()
