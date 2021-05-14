# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/8. 


class Solution(object):
    """
    4. Median of Two Sorted Arrays
    Hard

    9949

    1527

    Add to List

    Share
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.



    Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    Example 3:

    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000
    Example 4:

    Input: nums1 = [], nums2 = [1]
    Output: 1.00000
    Example 5:

    Input: nums1 = [2], nums2 = []
    Output: 2.00000


    Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106


    Follow up: The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays_merge(self, nums1, nums2):
        """
        Runtime: 76 ms, faster than 57.96% of Python online submissions for Median of Two Sorted Arrays.
        Memory Usage: 13.5 MB, less than 94.36% of Python online submissions for Median of Two Sorted Arrays.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if(0 == len_nums1 and 0 == len_nums2):
            return 0.
        total_len = len_nums1 + len_nums2
        if(0 == total_len % 2):
            rst_idx_left = (len_nums1 + len_nums2) / 2 - 1
            rst_idx_right = (len_nums1 + len_nums2) / 2
        else:
            rst_idx_left = rst_idx_right = (len_nums1 + len_nums2) / 2
        if(0 == len_nums1):
            return (nums2[rst_idx_left] + nums2[rst_idx_right]) / 2.
        if(0 == len_nums2):
            return (nums1[rst_idx_left] + nums1[rst_idx_right]) / 2.
        merged = sorted(nums1 + nums2)
        return (merged[rst_idx_left] + merged[rst_idx_right]) /2.

    def findMedianSortedArrays_tranverse(self, nums1, nums2):
        """
        Runtime: 72 ms, faster than 74.39% of Python online submissions for Median of Two Sorted Arrays.
        Memory Usage: 13.8 MB, less than 21.96% of Python online submissions for Median of Two Sorted Arrays.

        Runtime: 76 ms, faster than 57.82% of Python online submissions for Median of Two Sorted Arrays.
        Memory Usage: 13.6 MB, less than 75.84% of Python online submissions for Median of Two Sorted Arrays.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if(0 == len_nums1 and 0 == len_nums2):
            return 0.
        elif(1 == len_nums1 and 1 == len_nums2):
            return (nums1[0] + nums2[0]) / 2.
        total_len = len_nums1 + len_nums2
        if(0 == total_len % 2):
            rst_idx_left = (len_nums1 + len_nums2) / 2 - 1
            rst_idx_right = (len_nums1 + len_nums2) / 2
        else:
            rst_idx_left = rst_idx_right = (len_nums1 + len_nums2) / 2
        if(0 == len_nums1):
            return (nums2[rst_idx_left] + nums2[rst_idx_right]) / 2.
        if(0 == len_nums2):
            return (nums1[rst_idx_left] + nums1[rst_idx_right]) / 2.

        if(len_nums1 < len_nums2):
            # ensure nums1 is longer list
            len_nums1, len_nums2, nums1, nums2 = len_nums2, len_nums1, nums2, nums1

        rst_left = 0.
        rst_right = 0.
        total_point_left = -1
        point_1 = point_2 = -1
        while(total_point_left < rst_idx_left):
            total_point_left += 1
            if(point_1 < len_nums1 -1 and point_2 < len_nums2-1):
                num1 = nums1[point_1 + 1]
                num2 = nums2[point_2 + 1]
                if(num1 <= num2):
                    point_1 += 1
                else:
                    if(point_2 < len_nums2 -1): point_2 += 1
                    else: point_1 += 1
            elif(point_1 < len_nums1):
                point_1 += 1
        """ 
        three situation：
        num1 start and num2 not start
        num1 start and num2 start and num2 end
        num1 start and num2 start and num2 not end
        
        num1 start and end and num2 not start
        num1 start and and end num2 start and num2 end
        num1 start and end and num2 start and num2 not end
        
        """
        if(point_1 == -1):
            # ensure nums1 is started list
            len_nums1, len_nums2, nums1, nums2 = len_nums2, len_nums1, nums2, nums1
            point_1, point_2 = point_2, point_1

        if(rst_idx_left == rst_idx_right):
            if(point_2 == -1):
                rst_left = rst_right = nums1[point_1]
            elif(point_1 == -1):
                rst_left = rst_right = nums2[point_2]
            # elif(point_2 == len_nums2 - 1):
            #         rst_left = rst_right = nums1[point_1] if(point_1 > point_2) else max(nums1[point_1], nums2[point_2])
            else:
                rst_left = rst_right = max(nums2[point_2], nums1[point_1])
        else:
            if(point_2 == -1):
                rst_left = nums1[point_1]
                rst_right = min(nums2[point_2 + 1], nums1[point_1 + 1]) if( (point_1 + 1) < len_nums1) else nums2[point_2+1]
            elif(point_2 == len_nums2 - 1):
                if(nums1[point_1] < nums2[point_2]):
                    rst_left = nums2[point_2]
                else:
                    rst_left = nums1[point_1]
                rst_right = nums1[point_1 + 1]
            else:
                rst_left = max(nums1[point_1], nums2[point_2])
                rst_right = min(nums1[point_1+1], nums2[point_2 + 1])

        return (rst_left + rst_right) /2.

    def median(self, A, B):
        """
        Runtime: 68 ms, faster than 87.08% of Python online submissions for Median of Two Sorted Arrays.
        Memory Usage: 13.8 MB, less than 22.05% of Python online submissions for Median of Two Sorted Arrays.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # return self.median(nums1, nums2)
        return self.findMedianSortedArrays_tranverse(nums1, nums2)
        # return self.findMedianSortedArrays_merge(nums1, nums2)

    def self_testing(self):
        assert self.findMedianSortedArrays([100001], [100000] ) == 100000.5
        assert self.findMedianSortedArrays([1], [2,3,4]) == 2.5
        assert self.findMedianSortedArrays([3,4], [1,2]) == 2.5
        assert self.findMedianSortedArrays([1,3],[2,7]) == 2.5
        assert self.findMedianSortedArrays([1,2],[3,4]) == 2.5
        assert self.findMedianSortedArrays([1,2,3],[4]) == 2.5
        assert self.findMedianSortedArrays([1,2],[3]) == 2.0
        assert self.findMedianSortedArrays([1],[2,3]) == 2.0
        assert self.findMedianSortedArrays([1,3],[2]) == 2.0
        assert self.findMedianSortedArrays([1,2,3],[]) == 2.0
        assert self.findMedianSortedArrays([1,2,3],[4,5]) == 3.0
        assert self.findMedianSortedArrays([1,2,3,4],[5]) == 3.0
        assert self.findMedianSortedArrays([0,0],[0,0]) == 0
        assert self.findMedianSortedArrays([],[1]) == 1
        assert self.findMedianSortedArrays([2],[]) == 2

Solution().self_testing()
