# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/11/11. 

class Solution(object):
    """
    409. Longest Palindrome
    Easy

    1335

    94

    Add to List

    Share
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



    Example 1:

    Input: s = "abccccdd"
    Output: 7
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
    Example 2:

    Input: s = "a"
    Output: 1
    Example 3:

    Input: s = "bb"
    Output: 2


    Constraints:

    1 <= s.length <= 2000
    s consits of lower-case and/or upper-case English letters only.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        Runtime: 28 ms, faster than 26.71% of Python online submissions for Longest Palindrome.
        Memory Usage: 13.6 MB, less than 34.47% of Python online submissions for Longest Palindrome.
        """
        len_s = len(s)
        if(len_s < 1):
            return 0
        if(len_s < 2):
            return 1
        letter_count = {}
        for c in s:
            letter_count[c] = letter_count.get(c, 0) + 1
        pivot_flag = False
        max_odd_count = 0
        next_odd_count = 0
        half_result = 0
        letter_count_values = sorted(letter_count.values(), reverse=True)
        for x in letter_count_values:
            if(x % 2 == 0):
                half_result += x
            else:
                pivot_flag = True
                if(x > 1):
                    half_result += (x - 1)

        max_concact_result = half_result if(not pivot_flag) else half_result + 1

        return max_concact_result

    def self_testing(self):
        print(self.longestPalindrome("bananas"))
        print(self.longestPalindrome("cccaabbddddd"))
        print(self.longestPalindrome("abccccdd"))
        print(self.longestPalindrome("a"))
        print(self.longestPalindrome("bb"))
        print(self.longestPalindrome("ccc"))


Solution().self_testing()