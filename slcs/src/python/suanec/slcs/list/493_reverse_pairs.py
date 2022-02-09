# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2022/1/6.
class Solution(object):
    '''
    493. Reverse Pairs
    Hard

    2292

    168

    Add to List

    Share
    Given an integer array nums, return the number of reverse pairs in the array.

    A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].



    Example 1:

    Input: nums = [1,3,2,3,1]
    Output: 2 [3,1] [3,1]

    Example 2:

    Input: nums = [2,4,3,5,1]
    Output: 3


    Constraints:

    1 <= nums.length <= 5 * 10^4
    -231 <= nums[i] <= 2^31 - 1
    Accepted
    72,441
    Submissions
    247,671
    '''
    def value_index_inverted_index(self, _nums):
        inverted_index = {}
        for (idx, value) in enumerate(_nums):
            value_index_list = inverted_index.get(value, [])
            value_index_list.append(idx)
            inverted_index[value] = value_index_list
        inverted_index_keys = sorted(inverted_index.keys())
        return inverted_index_keys, inverted_index

    def judge_reverse_pairs(self, cur_idx, cur_value, other_idx, other_value):
        '''
        0 <= i < j < nums.length and nums[i] > 2 * nums[j]
        :param cur_idx:
        :param cur_value:
        :param other_idx:
        :param other_value:
        :return:
        '''
        if(cur_idx < other_idx):
            if(cur_value > 2 * other_value):
                return True
        return False

    def reversePairs(self, nums):
        """
        :param nums:
        :return:
        """
        # return self.reversePairs_tranverse_TLE(nums)
        return self.reversePairs_merge_sort(nums)


    def reversePairs_tranverse_TLE(self, nums):
        """
        Time Limit Exceeded
        :type nums: List[int]
        :rtype: int
        """
        reverse_pair_count = 0
        for (cur_idx, cur_value) in enumerate(nums):
            other_base_idx = cur_idx + 1
            for (other_idx, other_value) in enumerate(nums[other_base_idx:]):
                if(self.judge_reverse_pairs(cur_idx, cur_value, other_idx + other_base_idx, other_value)):
                    reverse_pair_count += 1
        return reverse_pair_count

    def reversePairs_merge_sort(self, nums):
        """
        # return self.reversePairsSub(nums, 0, len(nums)-1)
        Runtime: 1758 ms, faster than 75.51% of Python online submissions for Reverse Pairs.
        Memory Usage: 19.6 MB, less than 50.00% of Python online submissions for Reverse Pairs.
        return self.reversePairsSelf(nums, 0, len(nums) -1)
        Runtime: 2100 ms, faster than 65.31% of Python online submissions for Reverse Pairs.
        Memory Usage: 19.9 MB, less than 32.65% of Python online submissions for Reverse Pairs.

        :param nums:
        :return:
        """
        # return self.reversePairsSub(nums, 0, len(nums)-1)
        return self.reversePairsSelf(nums, 0, len(nums) -1)

    def reversePairsSub(self, nums, left, right):
        '''
        private int reversePairsSub(int[] nums, int l, int r) {
            if (l >= r) return 0;

            int m = l + ((r - l) >> 1);
            int res = reversePairsSub(nums, l, m) + reversePairsSub(nums, m + 1, r);

            int i = l, j = m + 1, k = 0, p = m + 1;
            int[] merge = new int[r - l + 1];

            while (i <= m) {
                while (p <= r && nums[i] > 2 L * nums[p]) p++;
                res += p - (m + 1);

                while (j <= r && nums[i] >= nums[j]) merge[k++] = nums[j++];
                merge[k++] = nums[i++];
            }

            while (j <= r) merge[k++] = nums[j++];

            System.arraycopy(merge, 0, nums, l, merge.length);

            return res;
        }
        :param left:
        :param right:
        :return:
        '''
        if(left >= right): return 0

        middle = left + ((right - left) >> 1)
        rst = self.reversePairsSub(nums, left, middle) + self.reversePairsSub(nums, middle + 1, right)

        i,j,k,p = left, middle + 1, 0, middle + 1
        merge = [0] * (right - left + 1)
        while(i <= middle):
            while(p <= right and nums[i] > 2 * nums[p]): p += 1
            rst += p - (middle + 1)

            while(j <= right and nums[i] >= nums[j]) :
                merge[k] = nums[j]
                k += 1
                j += 1
            merge[k] = nums[i]
            k += 1; i += 1
        while(j <= right):
            merge[k] = nums[j]
            k += 1
            j += 1
        nums[left:left + len(merge)] = merge[0:]
        return rst

    def reversePairsSelf(self, nums, left, right):
        if(left >= right): return 0

        middle = left + ((right - left) >> 1)
        # divide input array into two parts
        # and check count of important reverse pairs in each subarray
        # last sort which is merge sort each subarray overwrite the origin input array. asc order
        # result is sum of two count of important reverse pairs in each subarray
        result = self.reversePairsSelf(nums, left, middle) + self.reversePairsSelf(nums, middle + 1, right)

        # then use sorted nums to check important reverse pairs in cur input array nums.
        i = left; j = p = middle + 1; k = 0
        merge = [0] * (right - left + 1)

        while(i <= middle):
            p = middle + 1
            while(p <= right and nums[i] > 2 * nums[p]):
                p += 1
                result += 1
            """
            more efficient:
            while(p <= right and nums[i] > 2 * nums[p]):
                p += 1
            result += p - (middle + 1)
            because left and right two subarray both ordered.
            that ensured nums[i] > nums[i-1], and num[p] > num[p-1]
            so while nums[i] > 2 * num[p], nums[i] > 2 * nums[p] > 2 * nums[p-1]   
            from this we can found: we need not tranverse the part of right subarray before p
            but the result need add (p - p_start) equals to p - (middle + 1), 
            contain the left part of right subarray before p
            """

            while(j <= right and nums[i] > nums[j]):
                merge[k] = nums[j]
                k += 1; j += 1
            merge[k] = nums[i]
            k += 1; i += 1
        while(j <= right):
            merge[k] = nums[j]
            k += 1; j += 1

        nums[left:right + 1] = merge
        return result




    def self_testing(self):
        # print(self.value_index_inverted_index([1,3,2,3,1]))
        # 2
        print(self.reversePairs([1,3,2,3,1]))
        # 3
        print(self.reversePairs([2,4,3,5,1]))
        # 0
        print(self.reversePairs([]))

Solution().self_testing()