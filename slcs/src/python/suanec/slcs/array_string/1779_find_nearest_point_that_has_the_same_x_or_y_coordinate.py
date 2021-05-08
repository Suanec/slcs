# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/8. 

class Solution(object):
    """
    1779. Find Nearest Point That Has the Same X or Y Coordinate
    Easy

    90

    18

    Add to List

    Share
    You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
    You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
    A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

    Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
    If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).



    Example 1:

    Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    Output: 2
    Explanation:
    Of all the points, only [3,1], [2,4] and [4,4] are valid.
    Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location,
    with a distance of 1. [2,4] has the smallest index, so return 2.
    Example 2:

    Input: x = 3, y = 4, points = [[3,4]]
    Output: 0
    Explanation: The answer is allowed to be on the same location as your current location.
    Example 3:

    Input: x = 3, y = 4, points = [[2,3]]
    Output: -1
    Explanation: There are no valid points.


    Constraints:

    1 <= points.length <= 104
    points[i].length == 2
    1 <= x, y, ai, bi <= 104
    """
    def nearestValidPoint(self, x, y, points):
        """
        with sorted
        Runtime: 620 ms, faster than 14.40% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
        Memory Usage: 18.6 MB, less than 96.71% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.

        without sorted
        Runtime: 592 ms, faster than 77.78% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
        Memory Usage: 18.8 MB, less than 82.72% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.

        Runtime: 580 ms, faster than 95.47% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
        Memory Usage: 19 MB, less than 34.16% of Python online submissions for Find Nearest Point That Has the Same X or Y Coordinate.

        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        rst_idx_memo = {}
        smallest_manhattan_distance = float('inf')
        for (idx, point) in enumerate(points):
            [px,py] = point
            if(px == x or py == y):
                cur_manhattan_dist = abs(px - x) + abs(py - y)
                if(cur_manhattan_dist == smallest_manhattan_distance):
                    rst_idx_memo[cur_manhattan_dist] = rst_idx_memo.get(cur_manhattan_dist, []) + [idx]
                elif(cur_manhattan_dist < smallest_manhattan_distance):
                    smallest_manhattan_distance = cur_manhattan_dist
                    rst_idx_memo[cur_manhattan_dist] = [idx]
        return rst_idx_memo.get(smallest_manhattan_distance, [-1])[0]

    def self_testing(self):
        print(self.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
        print(self.nearestValidPoint(3,4,[[3,4]]))
        print(self.nearestValidPoint(3,4,[[2,3]]))

Solution().self_testing()
