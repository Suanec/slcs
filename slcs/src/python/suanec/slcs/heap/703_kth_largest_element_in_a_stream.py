# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/6. 

import heapq
class KthLargest(object):
    """
    703. Kth Largest Element in a Stream
    Easy

    1228

    752

    Add to List

    Share
    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Returns the element representing the kth largest element in the stream.


    Example 1:

    Input
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

    Explanation
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8


    Constraints:

    1 <= k <= 104
    0 <= nums.length <= 104
    -104 <= nums[i] <= 104
    -104 <= val <= 104
    At most 104 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.
    """

    """
    Runtime: 92 ms, faster than 90.06% of Python online submissions for Kth Largest Element in a Stream.
    Memory Usage: 17.6 MB, less than 92.61% of Python online submissions for Kth Largest Element in a Stream.
    """
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)


    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

    """
    Runtime: 100 ms, faster than 65.91% of Python online submissions for Kth Largest Element in a Stream.
    Memory Usage: 17.9 MB, less than 25.00% of Python online submissions for Kth Largest Element in a Stream.
    """
    def __init_self__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.inner_heap = []
        self.k = k
        for elem in nums:
            heapq.heappush(self.inner_heap, elem)
            if(len(self.inner_heap) > k):
                heapq.heappop(self.inner_heap)

    def add_self(self, val):
        """
        :type val: int
        :rtype: int
        """
        if(len(self.inner_heap) < self.k):
            heapq.heappush(self.inner_heap, val)
            rst = self.inner_heap[0]
        else:
            rst = self.inner_heap[0]
            if(val > rst):
                rst = heapq.heappop(self.inner_heap)
                heapq.heappush(self.inner_heap, val)
                rst = self.inner_heap[0]

        return rst




        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
    def self_testing(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2]);
        print(kthLargest.add(3));   # return 4
        print(kthLargest.add(5));   # return 5
        print(kthLargest.add(10));  # return 5
        print(kthLargest.add(9));   # return 8
        print(kthLargest.add(4));   # return 8
        print()

        kthLargest = KthLargest(1,[])
        print(kthLargest.add(-3))
        print(kthLargest.add(-2))
        print(kthLargest.add(-4))
        print(kthLargest.add(0))
        print(kthLargest.add(4))
        print()

        kthLargest = KthLargest(2,[0])
        print(kthLargest.add(-1))
        print(kthLargest.add(1))
        print(kthLargest.add(-2))
        print(kthLargest.add(-4))
        print(kthLargest.add(3))
        print()

        kthLargest = KthLargest(3,[5,-1])
        print(kthLargest.add(2))
        print(kthLargest.add(1))
        print(kthLargest.add(-1))
        print(kthLargest.add(3))
        print(kthLargest.add(4))
        print()

KthLargest(1,[]).self_testing()
