# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/3/5. 

class Solution(object):
    '''
    299. Bulls and Cows
    Medium

    913

    1023

    Add to List

    Share
    You are playing the Bulls and Cows game with your friend.

    You write down a secret number and ask your friend to guess what the number is.
    When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows",
    which are digits in the guess that are in your secret number but are located in the wrong position.
    Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
    Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
    Note that both secret and guess may contain duplicate digits.



    Example 1:

    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1807"
      |
    "7810"
    Example 2:

    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1123"        "1123"
      |      or     |
    "0111"        "0111"
    Note that only one of the two unmatched 1s is counted as a cow since
    the non-bull digits can only be rearranged to allow one 1 to be a bull.
    Example 3:

    Input: secret = "1", guess = "0"
    Output: "0A0B"
    Example 4:

    Input: secret = "1", guess = "1"
    Output: "1A0B"


    Constraints:

    1 <= secret.length, guess.length <= 1000
    secret.length == guess.length
    secret and guess consist of digits only.
    Accepted
    206,461
    Submissions
    463,767
    '''
    def getHint(self, secret, guess):
        """
        Runtime: 24 ms, faster than 94.97% of Python online submissions for Bulls and Cows.
        Memory Usage: 13.8 MB, less than 7.54% of Python online submissions for Bulls and Cows.
        :type secret: str
        :type guess: str
        :rtype: str
        """
        rst_fmt = "{bull}A{cow}B"
        secret_digit_table = {}
        guess_digit_table = {}
        length = len(secret)
        if(length < 1):
            return rst_fmt.format(bull = 0, cow = 0)
        bull_x = 0
        for (secret_char, guess_char) in zip(secret, guess):
            if(secret_char == guess_char):
                bull_x += 1
            else:
                secret_digit_table[secret_char] = secret_digit_table.get(secret_char,0) + 1
                guess_digit_table[guess_char] = guess_digit_table.get(guess_char,0) + 1
        if(length == bull_x):
            return rst_fmt.format(bull = bull_x, cow = 0)

        else:
            cow_y = 0
            for (guess_char, guess_char_value) in guess_digit_table.items():
                secret_char_value = secret_digit_table.get(guess_char,0)
                cow_y += min([secret_char_value, guess_char_value])
        return rst_fmt.format(bull = bull_x, cow = cow_y)

    def self_testing(self):
        print(self.getHint("1807", "7810"))
        print(self.getHint("1123", "0111"))
        print(self.getHint("1", "0"))
        print(self.getHint("1", "1"))
        print(self.getHint("", ""))

Solution().self_testing()
