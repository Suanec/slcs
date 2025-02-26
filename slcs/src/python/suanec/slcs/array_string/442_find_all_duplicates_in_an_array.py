# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2025/2/26.
# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/8/17.

import random
def gen_lis(num):
    li = []
    cnt_dict = {}
    i = random.randint(1,num)
    while(len(li) < num):
        if(cnt_dict.get(i, -1) < 2):
            li.append(i)
            cnt_dict[i] = cnt_dict.get(i,0) + 1
        i = random.randint(1,num)
    print(f"{'='*33}\norigin : {li}")
    print(f"result : {sorted([x for x,y in cnt_dict.items() if y > 1])}")
    return li

class Solution(object):
    '''
    # Given an integer array nums of length n where all the integers of nums are in
    # the range [1, n] and each integer appears at most twice, return an array of all
    # the integers that appears twice.
    #
    #  You must write an algorithm that runs in O(n) time and uses only constant
    # auxiliary space, excluding the space needed to store the output
    #
    #
    #  Example 1:
    #  Input: nums = [4,3,2,7,8,2,3,1]
    # Output: [2,3]
    #
    #  Example 2:
    #  Input: nums = [1,1,2]
    # Output: [1]
    #
    #  Example 3:
    #  Input: nums = [1]
    # Output: []
    #
    #
    #  Constraints:
    #
    #
    #  n == nums.length
    #  1 <= n <= 10⁵
    #  1 <= nums[i] <= n
    #  Each element in nums appears once or twice.
    #
    #
    #  Related Topics Array Hash Table 👍 10707 👎 420


    # leetcode submit region begin(Prohibit modification and deletion)
    class Solution(object):
        def findDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """

    # leetcode submit region end(Prohibit modification and deletion)

    '''

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = list()
        for cur_value in nums:
            target_idx = abs(cur_value) - 1
            if(nums[target_idx] > 0): nums[target_idx] = -nums[target_idx]
            else: rst.append(abs(cur_value))
        return rst

    def self_testing(self):
        for x in range(100):
            print(f"calced : {sorted(self.findDuplicates(gen_lis(random.randint(10,100))))}")

if __name__ == '__main__':

    s = Solution()
    s.self_testing()