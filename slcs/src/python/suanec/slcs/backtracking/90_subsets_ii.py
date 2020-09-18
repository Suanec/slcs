# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/9/7. 

class Solution(object):
    """
    Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:

    Input: [1,2,2]
    Output:
    [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
    ]
    """
    def subsetsWithDup_from_discuss(self, nums):
        """
        To solve this problem,
        it is helpful to first thlink how many subsets are there.
        If there is no duplicate element,
        the answer is simply 2^n, where n is the number of elements.
        This is because you have two choices for each element,
        either putting it into the subset or not.
        So all subsets for this no-duplicate set can be easily constructed:
        num of subset

        (1 to 2^0) empty set is the first subset
        (2^0+1 to 2^1) add the first element into subset from (1)
        (2^1+1 to 2^2) add the second element into subset (1 to 2^1)
        (2^2+1 to 2^3) add the third element into subset (1 to 2^2)
        ....
        (2^(n-1)+1 to 2^n) add the nth element into subset(1 to 2^(n-1))

        Then how many subsets are there if there are duplicate elements?
        We can treat duplicate element as a spacial element.
        For example, if we have duplicate elements (5, 5),
        instead of treating them as two elements that are duplicate,
        we can treat it as one special element 5,
        but this element has more than two choices:
        you can either NOT put it into the subset, or put ONE 5 into the subset, or put TWO 5s into the subset.
        Therefore, we are given an array (a1, a2, a3, ..., an) with each of them appearing (k1, k2, k3, ..., kn) times,
        the number of subset is (k1+1)(k2+1)...(kn+1).
        We can easily see how to write down all the subsets similar to the approach above.

        class Solution {
            public:
                vector<vector<int> > subsetsWithDup(vector<int> &S) {
                    vector<vector<int> > totalset = {{}};
                    sort(S.begin(),S.end());
                    for(int i=0; i<S.size();){
                        int count = 0; // num of elements are the same
                        while(count + i<S.size() && S[count+i]==S[i])  count++;
                        int previousN = totalset.size();
                        for(int k=0; k<previousN; k++){
                            vector<int> instance = totalset[k];
                            for(int j=0; j<count; j++){
                                instance.push_back(S[i]);
                                totalset.push_back(instance);
                            }
                        }
                        i += count;
                    }
                    return totalset;
                }
            };
        };
        :param nums:
        :return:
        """
        import collections
        res = [[]]
        for num, freq in collections.Counter(nums).items():
            res_len = len(res)
            for i in range(1, freq+1):
                for r in res[:res_len]:
                    res.append(r+[num]*i)
        return res

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return self.subset_with_dup_set(nums)
        return self.subset_dp(nums)

    def subset_with_dup_set(self, nums):
        nums_distinct = list(set(nums))
        return self.subset(nums_distinct)

    def subset(self, nums):
        pass

    def subset_dp(self, nums):
        results = [[]]
        if(len(nums) < 1):return results
        global_dict = {}

        for cur_p in nums:
            result = []
            rst = []
            for (num_key, sub_set) in global_dict.items():
                rst = []
                [rst.append(list(x)) for x in sub_set]
                for i in rst:
                    i.append(cur_p)
                result += rst
            # result.append([])
            result.append([cur_p])
            global_dict[cur_p] = result
            results += result
        return results

    def self_testing(self):
        print self.subsetsWithDup([1,2,2])

if __name__ == '__main__':
    s = Solution()
    s.self_testing()
