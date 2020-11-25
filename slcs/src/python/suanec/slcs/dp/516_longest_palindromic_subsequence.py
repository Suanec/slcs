# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/11/21. 

class Solution(object):
    """
    516. Longest Palindromic Subsequence
    Medium

    2515

    202

    Add to List

    Share
    Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input:

    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".


    Example 2:
    Input:

    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".


    Constraints:

    1 <= s.length <= 1000
    s consists only of lowercase English letters.
    """
    def longestPalindromeSubseq(self, s):
        """
        Runtime: 920 ms, faster than 91.40% of Python online submissions for Longest Palindromic Subsequence.
        Memory Usage: 13.4 MB, less than 98.77% of Python online submissions for Longest Palindromic Subsequence.

        :param s:
        :return:
        """
        len_s = len(s)
        if(len_s < 1):
            return 0
        if(len_s < 2):
            return 1
        cur_dp = [0] * len_s
        pre_dp = [0] * len_s
        for left in xrange(len_s -1 , -1, -1):
            cur_dp[left] = 1
            for right in xrange(left + 1, len_s):
                if(s[left] == s[right]):
                    cur_dp[right] = pre_dp[right -1] + 2
                else:
                    cur_dp[right] = max(cur_dp[right-1], pre_dp[right])
            pre_dp = cur_dp
            cur_dp = [0] * len_s
        return pre_dp[len_s - 1]

    def longestPalindromeSubseq_v1(self, s):
        """
        :type s: str
        :rtype: int
        Runtime: 1212 ms, faster than 87.35% of Python online submissions for Longest Palindromic Subsequence.
        Memory Usage: 28.3 MB, less than 73.45% of Python online submissions for Longest Palindromic Subsequence.
        public class Solution {
            public int longestPalindromeSubseq(String s) {
                int[][] dp = new int[s.length()][s.length()];

                for (int i = s.length() - 1; i >= 0; i--) {
                    dp[i][i] = 1;
                    for (int j = i+1; j < s.length(); j++) {
                        if (s.charAt(i) == s.charAt(j)) {
                            dp[i][j] = dp[i+1][j-1] + 2;
                        } else {
                            dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
                        }
                    }
                }
                return dp[0][s.length()-1];
            }
        }
        """
        len_s = len(s)
        if(len_s < 1):
            return 0
        if(len_s < 2):
            return 1
        dp = []
        for i in xrange(0,len_s):
            dp.append([0] * len_s)
        for left in xrange(len_s -1, -1, -1):
            dp[left][left] = 1
            for right in xrange(left + 1, len_s):
                if(s[left] == s[right]):
                    dp[left][right] = dp[left+1][right -1] + 2
                else:
                    dp[left][right] = max(dp[left][right-1], dp[left+1][right])
        return dp[0][len_s-1]

    def self_testing(self):
        print(self.longestPalindromeSubseq("bbbab"))

Solution().self_testing()