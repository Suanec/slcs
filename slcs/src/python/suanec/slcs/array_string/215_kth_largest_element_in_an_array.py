# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/4/30. 

class Solution(object):
    """
    215. Kth Largest Element in an Array
    Medium

    5555

    355

    Add to List

    Share
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.



    Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4


    Constraints:

    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104

    """
    def findMinium(self, nums):
        min_num = float('inf')
        for elem in nums:
            if(elem < min_num):
                min_num = elem
        return min_num

    def findKthLargest_buildin(self, nums, k):
        """
        Runtime: 40 ms, faster than 97.69% of Python online submissions for Kth Largest Element in an Array.
        Memory Usage: 14.3 MB, less than 37.77% of Python online submissions for Kth Largest Element in an Array.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(len(nums) <= k):
            return self.findMinium(nums)
        return sorted(nums)[-k]

    def findKthLargest_buildin_heap(self, nums, k):
        """
        Runtime: 72 ms, faster than 34.04% of Python online submissions for Kth Largest Element in an Array.
        Memory Usage: 14.2 MB, less than 60.45% of Python online submissions for Kth Largest Element in an Array.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(len(nums) <= k):
            """
            Runtime: 60 ms, faster than 45.78% of Python online submissions for Kth Largest Element in an Array.
            Memory Usage: 14.4 MB, less than 37.77% of Python online submissions for Kth Largest Element in an Array.
            """
            return self.findMinium(nums)
        heap=[]
        import heapq
        for i in nums:
            heapq.heappush(heap,i)       #top element of stack will always be minimum
            if len(heap)>k:
                heapq.heappop(heap)           #if length of stack is more then k then pop top most element from stack

        return(heapq.heappop(heap))

    def findKthLargest(self, nums, k):
        """
        quick_select method
        :param nums:
        :param k:
        :return:
        """
        return self.quick_select(nums, k)

    def quick_select(self, nums, k):
        '''
        Runtime: 56 ms, faster than 53.03% of Python online submissions for Kth Largest Element in an Array.
        Memory Usage: 14.3 MB, less than 60.10% of Python online submissions for Kth Largest Element in an Array.
        :param nums:
        :param k:
        :return:
        '''
        if(len(nums) <= k):
            return self.findMinium(nums)
        max_idx = len(nums)-1

        """
        public int findKthLargest(int[] nums, int k) {
          return quickSelect(nums, 0, nums.length - 1, k);
        }
        
        int quickSelect(int[] nums, int low, int high, int k) {
          int pivot = low;
        
          // use quick sort's idea
          // put nums that are <= pivot to the left
          // put nums that are  > pivot to the right
          for (int j = low; j < high; j++) {
            if (nums[j] <= nums[high]) {
              swap(nums, pivot++, j);
            }
          }
          swap(nums, pivot, high);
          
          // count the nums that are > pivot from high
          int count = high - pivot + 1;
          // pivot is the one!
          if (count == k) return nums[pivot];
          // pivot is too small, so it must be on the right
          if (count > k) return quickSelect(nums, pivot + 1, high, k);
          // pivot is too big, so it must be on the left
          return quickSelect(nums, low, pivot - 1, k - count);
        }
        """
        pivot_idx = 0

        for idx in xrange(0, max_idx):
            if(nums[idx] <= nums[max_idx]):
                nums[idx], nums[pivot_idx] = nums[pivot_idx], nums[idx]
                pivot_idx += 1

        nums[max_idx], nums[pivot_idx] = nums[pivot_idx], nums[max_idx]

        len_right_part = max_idx - pivot_idx + 1
        if(len_right_part > k):
            return self.findKthLargest(nums[pivot_idx + 1:], k)
        elif(len_right_part == k):
            return nums[pivot_idx]
        else:
            return self.findKthLargest(nums[:pivot_idx], k - len_right_part)

    def self_testing(self):
        print(self.findKthLargest([3,2,1,5,6,4], 2))
        print(self.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
        print(self.findKthLargest([9,20,10,-1], 2))


Solution().self_testing()

