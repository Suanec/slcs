# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/3/5. 
class Solution(object):
    """
    939. Minimum Area Rectangle
    Medium

    893

    171

    Add to List

    Share

    Given a set of points in the xy-plane,
    determine the minimum area of a rectangle formed from these points,
    with sides parallel to the x and y axes.

    If there isn't any rectangle, return 0.



    Example 1:

    Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: 4
    Example 2:

    Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    Output: 2


    Note:

    1 <= points.length <= 500
    0 <= points[i][0] <= 40000
    0 <= points[i][1] <= 40000
    All points are distinct.
    Accepted
    64,482
    Submissions
    124,132
    """
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if(len(points) < 4):
            return 0
        x_table = {}
        y_table = {}
        for point in points:
            x_table[point[0]] = x_table.get(point[0], []) + [point[1]]
            y_table[point[1]] = y_table.get(point[1], []) + [point[0]]
        for (x_axes, x_points) in x_table.items():
            if(len(x_points) < 2):
                x_table.pop(x_axes)
        for (y_axes, y_points) in y_table.items():
            if(len(y_points) < 2):
                y_table.pop(y_axes)

        x_axes = sorted(x_table.keys())
        y_axes = sorted(y_table.keys())



    def minAreaRect_from_discuss_O_N_2(self, points):
        """
        Runtime: 1216 ms, faster than 59.84% of Python online submissions for Minimum Area Rectangle.
        Memory Usage: 13.8 MB, less than 62.30% of Python online submissions for Minimum Area Rectangle.

        :type points: List[List[int]]
        :rtype: int
        """
        import sys
        min_area = sys.maxsize
        points_table = set()

        for x, y in points:
            points_table.add((x,y))

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2: # Skip looking at same point
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 -  x2) * abs(y1 - y2)
                        if area:
                            min_area = min(area, min_area)

        return 0 if min_area == sys.maxsize else min_area

    '''
    Solution 1, Brute force
    N = 500 is really loose.
    Just check all pairs of points.
    Time O(N^2) , 1000ms ~ 1200ms
    
    Python
    
        def minAreaRect(self, points):
        """
        Runtime: 1212 ms, faster than 60.25% of Python online submissions for Minimum Area Rectangle.
        Memory Usage: 13.6 MB, less than 99.18% of Python online submissions for Minimum Area Rectangle.
        """
            seen = set()
            res = float('inf')
            for x1, y1 in points:
                for x2, y2 in seen:
                    if (x1, y2) in seen and (x2, y1) in seen:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        if area and area < res:
                            res = area
                seen.add((x1, y1))
            return res if res < float('inf') else 0
    
    Solution 2
    Another idea is that,
    For each x value in sorted order, check all y pairs.
    
    In most cases, all points randomly distribute.
    Only 500 points in 40001 * 40001 possible coordinates.
    No two points will have the same x value or y value.
    There will be no rectangle and the result is 0.
    This will be O(N) solution.
    
    However, it seems that, in the test cases, it has a really big amount of rectangles.
    In these worst cases, the time complexity is O(nx * nx * ny) < O(N ^ 1.5).
    
    In the extreme worst cases, like all points have x = 0 or y = 0
    Time complexity will be O(N^2)
    
    Time O(N^1.5), 80ms
    
    
        def minAreaRect(self, points):
        """
        Runtime: 164 ms, faster than 99.59% of Python online submissions for Minimum Area Rectangle.
        Memory Usage: 13.8 MB, less than 62.30% of Python online submissions for Minimum Area Rectangle.
        """
            n = len(points)
            nx = len(set(x for x, y in points))
            ny = len(set(y for x, y in points))
            if nx == n or ny == n:
                return 0
    
            p = collections.defaultdict(list)
            if nx > ny:
                for x, y in points:
                    p[x].append(y)
            else:
                for x, y in points:
                    p[y].append(x)
    
            lastx = {}
            res = float('inf')
            for x in sorted(p):
                p[x].sort()
                for i in range(len(p[x])):
                    for j in range(i):
                        y1, y2 = p[x][j], p[x][i]
                        if (y1, y2) in lastx:
                            res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                        lastx[y1, y2] = x
            return res if res < float('inf') else 0
        '''

    def self_testing(self):
        print(self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
        print(self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

Solution().self_testing()
