# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/4.

class Solution(object):
    """
    Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

    Return a list of all possible strings we could create. You can return the output in any order.



    Example 1:

    Input: S = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
    Example 2:

    Input: S = "3z4"
    Output: ["3z4","3Z4"]
    Example 3:

    Input: S = "12345"
    Output: ["12345"]
    Example 4:

    Input: S = "0"
    Output: ["0"]


    Constraints:

    S will be a string with length between 1 and 12.
    S will consist only of letters or digits.
    """
    def letterCasePermutation(self, S):
        """
        Runtime: 40 ms, faster than 91.76% of Python online submissions for Letter Case Permutation.
        Memory Usage: 13.5 MB, less than 84.44% of Python online submissions for Letter Case Permutation.
        :type S: str
        :rtype: List[str]
        """
        result = []
        for characters in S:
            if(characters.isdigit()):
                if(result):
                    for idx in range(0,len(result)):
                       result[idx] = result[idx] + characters
                else:
                    result.append(characters)
            else:
                rst = []
                if(len(result) > 0):
                    for idx in range(0,len(result)):
                        rst.append(result[idx] + characters.upper())
                        result[idx] = result[idx] + characters.lower()
                else:
                    result.append(characters.lower())
                    result.append(characters.upper())
                result += rst
        return result

    def self_testing(self):
        print(self.letterCasePermutation("a1b2"))
        print(self.letterCasePermutation("3z4"))
        print(self.letterCasePermutation("12345"))
        print(self.letterCasePermutation("0"))

if __name__ == '__main__':
    s = Solution()
    s.self_testing()
