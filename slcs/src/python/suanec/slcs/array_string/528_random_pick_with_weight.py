# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/14. 

import random
class Solution(object):
    """
    528. Random Pick with Weight
    Medium

    1268

    2840

    Add to List

    Share
    You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

    We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1].
    pickIndex() should return the integer proportional to its weight in the w array.
    For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%)
    while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

    More formally, the probability of picking index i is w[i] / sum(w).



    Example 1:

    Input
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output
    [null,0]

    Explanation
    Solution solution = new Solution([1]);
    solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
    Example 2:

    Input
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output
    [null,1,1,1,1,0]

    Explanation
    Solution solution = new Solution([1, 3]);
    solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

    Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
    [null,1,1,1,1,0]
    [null,1,1,1,1,1]
    [null,1,1,1,0,0]
    [null,1,1,1,0,1]
    [null,1,0,1,0,0]
    ......
    and so on.


    Constraints:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
    """
    def __init__(self, w):
        """
        Runtime: 348 ms, faster than 26.79% of Python online submissions for Random Pick with Weight.
        Memory Usage: 24.2 MB, less than 5.29% of Python online submissions for Random Pick with Weight.
        :type w: List[int]
        """
        self.w = w
        self.len_w = len(self.w)
        self.sum_w = sum(self.w) if(self.len_w > 0) else 0
        self.avg_w = self.sum_w * 1.0 / self.len_w if(self.len_w > 0) else 0

        self.index_memo = [ x - self.avg_w for x in self.w ]
        self.prob_set = []
        for (idx, x) in enumerate(self.w):
            if(x >= self.avg_w):
                self.prob_set.append([(idx, self.avg_w)])
            else:
                self.prob_set.append([(idx, x)])

        self.employer_memo = []
        self.employee_memo = []
        for x in enumerate( self.index_memo ):
            if(x[1] < 0):
                self.employee_memo.append(x)
            elif(x[1] > 0):
                self.employer_memo.append(x)

        while len(self.employer_memo) > 0:
            (borrow_idx, could_borrow_prob) = self.employer_memo[0]
            if(round(could_borrow_prob, 4) < 1e-4):
                self.employer_memo.remove((borrow_idx, could_borrow_prob))
            while len(self.employee_memo):
                (idx, prob_list) = self.employee_memo[0]
                (_, prob_right_threshold) = self.prob_set[idx][-1]
                if(prob_right_threshold < self.avg_w):
                    need_borrow_prob = self.avg_w - prob_right_threshold
                    if(round(could_borrow_prob, 4) < round(need_borrow_prob, 4)):
                        self.employer_memo.remove((borrow_idx, could_borrow_prob))
                        self.index_memo[borrow_idx] = 0
                        self.prob_set[idx].append((borrow_idx, prob_right_threshold + could_borrow_prob))
                        self.index_memo[idx] = (self.avg_w - prob_right_threshold - could_borrow_prob)
                        self.employee_memo[0] = (idx, could_borrow_prob - need_borrow_prob)
                        (borrow_idx, could_borrow_prob) = self.employer_memo[0]
                    elif(round(could_borrow_prob, 4) >= round(need_borrow_prob, 4)):
                        remains_borrow_prob = round(could_borrow_prob - need_borrow_prob, 6)
                        self.employer_memo[0] = (borrow_idx, remains_borrow_prob)
                        (_, could_borrow_prob) = self.employer_memo[0]
                        if(remains_borrow_prob < 1e-6):
                            self.employer_memo.remove((borrow_idx, remains_borrow_prob))
                            could_borrow_prob = 0
                        self.index_memo[borrow_idx] = remains_borrow_prob
                        self.index_memo[idx] = 0
                        self.prob_set[idx].append((borrow_idx, self.avg_w))
                        self.employee_memo.remove((idx, prob_list))
                        break;

        self.random = random.Random()

    def get_index_with_weight(self):
        random_index = self.random.randrange(0, self.len_w)
        first_index_sorted_weight_candicates = self.prob_set[random_index]
        (idx, prob_right_threshold) = first_index_sorted_weight_candicates[0]
        if(len(first_index_sorted_weight_candicates) == 1):
            return idx
        second_random_index = self.random.random() * self.avg_w
        for (idx, prob_right_threshold) in first_index_sorted_weight_candicates:
            if(second_random_index < prob_right_threshold):
                return idx

    def pickIndex(self):
        """
        :rtype: int
        """
        # return self.w[self.get_random_index()]
        return self.get_index_with_weight()



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()

    def self_testing(self):
        w = [1]
        w = [1, 3]
        w = [10,7,8,10]
        w = [1, 3, 1]
        w = [7,3,1,7,4,1,2,8,5]
        w = [8,6,8,4,6,2,3,2,7,10,10]
        s = Solution(w)
        for i in xrange(10000):
            print(s.pickIndex())

Solution([1]).self_testing()
