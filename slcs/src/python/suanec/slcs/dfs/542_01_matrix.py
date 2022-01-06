# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2020/10/20. 

class Solution(object):
    '''
    Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

    The distance between two adjacent cells is 1.



    Example 1:

    Input:
    [[0,0,0],
     [0,1,0],
     [0,0,0]]

    Output:
    [[0,0,0],
     [0,1,0],
     [0,0,0]]
    Example 2:

    Input:
    [[0,0,0],
     [0,1,0],
     [1,1,1]]

    Output:
    [[0,0,0],
     [0,1,0],
     [1,2,1]]


    Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.
    '''
    def updateMatrix_rotate_4_times(self, matrix):
        answer = [[10000 * x for x in row] for row in matrix]
        for _ in range(4):
            for row in answer:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)
            answer = map(list, zip(*answer[::-1]))
        return answer

    def updateMatrix_bfs(self, matrix):

        # So this problem asks us to find the minimum distance of 0  from every cell with value 1,
        # BFS should ring in your mind and instead of our single-source BFS, we
        # Apply multiple source BFS.
        import collections
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # The distance to itself is 0 and add all sources here to queue
                    res[i][j] = 0
                    queue.append((i, j))
        # Now we start our BFS

        while queue:
            curI, curJ = queue.popleft()
            for i, j in dirs:
                neighBorI, neighBorJ = curI + i, curJ + j
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    res[neighBorI][neighBorJ] = res[curI][curJ] + 1
                    queue.append((neighBorI, neighBorJ))
        return res


    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        Runtime: 492 ms, faster than 97.40% of Python online submissions for 01 Matrix.
        Memory Usage: 16.5 MB, less than 8.33% of Python online submissions for 01 Matrix.

        class Solution {
        public:
            vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
                int m = matrix.size(), n = matrix[0].size();
                vector<vector<int>> res(m, vector<int>(n, INT_MAX - 1));
                for (int i = 0; i < m; ++i) {
                    for (int j = 0; j < n; ++j) {
                        if (matrix[i][j] == 0) res[i][j] = 0;
                        else {
                            if (i > 0) res[i][j] = min(res[i][j], res[i - 1][j] + 1);
                            if (j > 0) res[i][j] = min(res[i][j], res[i][j - 1] + 1);
                        }
                    }
                }
                for (int i = m - 1; i >= 0; --i) {
                    for (int j = n - 1; j >= 0; --j) {
                        if (res[i][j] != 0 && res[i][j] != 1) {
                            if (i < m - 1) res[i][j] = min(res[i][j], res[i + 1][j] + 1);
                            if (j < n - 1) res[i][j] = min(res[i][j], res[i][j + 1] + 1);
                        }
                    }
                }
                return res;
            }
        };
        """
        cur_max_int = 10000
        if(len(matrix) < 1):
            return [[]]
        if(len(matrix[0]) < 1):
            return [[]]
        rst_matrix = [
            [
                0 if(0 == elem) else cur_max_int for elem in row
            ] for row in matrix
        ]
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])
        for row_idx in range(0,row_cnt):
            for col_idx in range(0, col_cnt):
                pre_row = row_idx -1 if(row_idx > 0) else 0
                pre_col = col_idx -1 if(col_idx > 0) else 0
                if(0 != rst_matrix[row_idx][col_idx]):
                    rst_matrix[row_idx][col_idx] = min(
                        rst_matrix[row_idx][col_idx], rst_matrix[pre_row][col_idx] + 1, rst_matrix[row_idx][pre_col] + 1
                    )

        for row_idx in range(row_cnt-1,-1,-1):
            for col_idx in range(col_cnt-1,-1,-1):
                pre_row = row_idx +1 if(row_idx < row_cnt-1) else row_cnt -1
                pre_col = col_idx +1 if(col_idx < col_cnt-1) else col_cnt -1
                if(0 != rst_matrix[row_idx][col_idx]):
                    rst_matrix[row_idx][col_idx] = min(
                        rst_matrix[row_idx][col_idx], rst_matrix[pre_row][col_idx] + 1, rst_matrix[row_idx][pre_col] + 1
                    )

        return rst_matrix

    def self_testing(self):
        print(self.updateMatrix([]))
        print(self.updateMatrix([[],[],[]]))
        # [[0,0,0], [0,1,0], [1,2,1]]
        print(self.updateMatrix([[0,0,0], [0,1,0], [1,1,1]]))
        # [[1,2,1],[0,1,0],[1,2,1]]
        print(self.updateMatrix([[1,1,1], [0,1,0], [1,1,1]]))
        # [[2,1,2],[1,0,1],[2,1,2]]
        print(self.updateMatrix([[1,1,1], [1,0,1], [1,1,1]]))

if __name__ == '__main__':
    Solution().self_testing()