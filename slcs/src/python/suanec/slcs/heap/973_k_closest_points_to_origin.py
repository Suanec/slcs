# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/8. 

import heapq
class Solution(object):
    """
    973. K Closest Points to Origin
    Medium

    3005

    156

    Add to List

    Share
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



    Example 1:


    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
    Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.


    Constraints:

    1 <= k <= points.length <= 104
    -104 < xi, yi < 104
    """

    def kClosest(self, points, k):
        """
        Runtime: 520 ms, faster than 97.56% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 18.9 MB, less than 100.00% of Python online submissions for K Closest Points to Origin.

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key= lambda (x, y): (x * x + y * y))[:k]

    def kClosest_large(self, points, k):
        """
        Runtime: 580 ms, faster than 64.94% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 19.8 MB, less than 43.75% of Python online submissions for K Closest Points to Origin.

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nlargest(k, points, lambda (x, y): -(x * x + y * y))

    def kClosest_small(self, points, k):
        """
        Runtime: 540 ms, faster than 85.17% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 19.5 MB, less than 60.45% of Python online submissions for K Closest Points to Origin.

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, points, lambda (x, y): x * x + y * y)

    def kClosest_self(self, points, k):
        """
        Runtime: 688 ms, faster than 13.86% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 20.2 MB, less than 25.51% of Python online submissions for K Closest Points to Origin.

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.inner_heap = []
        self.point_memo = {} # square_distance : [point1 , point2]
        for point in points:
            [x,y] = point
            square_distance_of_point = -(x ** 2 + y ** 2)
            self.point_memo[square_distance_of_point] = self.point_memo.get(square_distance_of_point, []) + [point]
            heapq.heappush(self.inner_heap, square_distance_of_point)
            if(len(self.inner_heap) > k):
                heapq.heappop(self.inner_heap)
        rst_list = []
        for square_distance_of_point in self.inner_heap:
            point_list = self.point_memo.get(square_distance_of_point, [])
            if(len(point_list) > 0):
                rst_list.append(point_list.pop(0))
        return rst_list

    def self_testing(self):
        print(self.kClosest([[3,3],[5,-1],[-2,4]],2))
        print(self.kClosest([[1,3],[-2,2]],1))
        print(self.kClosest([[2,2],[-2,2], [1,3]],3))

Solution().self_testing()
