# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2022/2/11.
class Solution(object):
    '''
    36. Valid Sudoku
    Medium

    4414

    670

    Add to List

    Share
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


    Example 1:


    Input: board =
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
    Example 2:

    Input: board =
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


    Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
    Accepted
    664,325
    Submissions
    1,222,337
    '''
    def isValidRow_naive(self, row):
        if(len(row) != 9):
            return False
        all_deduplicated = set(row)
        number_deduplicated = [x for x in row if "." != x]
        if(len(all_deduplicated) != len(number_deduplicated) +1):
            return False
        return True

    def isValidRow(self, row):
        inner_set = set()
        for elem in row:
            if("." != elem):
                if(elem in inner_set):
                    return False
                inner_set.add(elem)
        return True

    def isValidMatrix_naive(self, matrix):
        if(len(matrix) != 3):
            return False
        from functools import reduce
        mock_row = reduce(lambda x,y : x + y, matrix)
        return self.isValidRow(mock_row)

    def isValidMatrix(self, matrix):
        inner_set = set()
        for row in matrix:
            for elem in row:
                if("." != elem):
                    if(elem in inner_set):
                        return False
                inner_set.add(elem)
        return True

    def isValidSudoku_naive(self, board):
        """
        naive
        Runtime: 146 ms, faster than 18.00% of Python online submissions for Valid Sudoku.
        Memory Usage: 13.6 MB, less than 46.36% of Python online submissions for Valid Sudoku.

        judgement_cleansing
        Runtime: 124 ms, faster than 34.94% of Python online submissions for Valid Sudoku.
        Memory Usage: 13.5 MB, less than 72.11% of Python online submissions for Valid Sudoku.

        isValidSudoku_remove_check_and_judge_cleansing(self, board):
        :type board: List[List[str]]
        :rtype: bool
        """
        if(9 != len(board)):
            return False
        max_col = 0
        for row in board:
            max_col = max(max_col, len(row))
            if(False == self.isValidRow(row)):
                return False
        if(9 != max_col):
            return False
        for col_idx in range(0, max_col):
            column = []
            for row_idx in range(0,len(board)):
                column.append(board[row_idx][col_idx])
            if(False == self.isValidRow(column)):
                return False
        matrix_step = 3
        cur_matrix_row_idx = 0
        cur_matrix_col_idx = 0
        matrix = []
        while(cur_matrix_row_idx <= len(board) - matrix_step):
            for row_idx in range(cur_matrix_row_idx, cur_matrix_row_idx + matrix_step):
                matrix_row = []
                matrix_row_idx = row_idx - cur_matrix_row_idx
                for col_idx in range(cur_matrix_col_idx, cur_matrix_col_idx + matrix_step):
                    matrix_row.append(board[row_idx][col_idx])
                matrix.append(matrix_row)
            if(False == self.isValidMatrix(matrix)):
                return False
            matrix = []
            if(cur_matrix_col_idx >= max_col - matrix_step):
                cur_matrix_row_idx += matrix_step
                cur_matrix_col_idx = 0
            else:
                cur_matrix_col_idx += matrix_step
        return True

    def isValidSudoku_remove_check_and_judge_cleansing(self, board):
        max_col = 9
        matrix_step = 3
        cur_matrix_row_idx = 0
        cur_matrix_col_idx = 0
        matrix = []
        row_set = []
        col_set = []
        matrix_set = []
        while(cur_matrix_row_idx <= len(board) - matrix_step):
            for row_idx in range(cur_matrix_row_idx, cur_matrix_row_idx + matrix_step):
                matrix_row = []
                for col_idx in range(cur_matrix_col_idx, cur_matrix_col_idx + matrix_step):
                    matrix_row.append(board[row_idx][col_idx])
                matrix.append(matrix_row)
            if(False == self.isValidMatrix(matrix)):
                return False
            matrix = []
            if(cur_matrix_col_idx >= max_col - matrix_step):
                cur_matrix_row_idx += matrix_step
                cur_matrix_col_idx = 0
            else:
                cur_matrix_col_idx += matrix_step
        return True

    def isValidSudoku(self, board):
        # return self.isValidSudoku_naive(board)
        return self.isValidSudoku_remove_check_and_judge_cleansing(board)


    def self_testing(self):
        board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        print(self.isValidSudoku(board=board))
        board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        print(self.isValidSudoku(board=board))
        board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
        # False
        print(self.isValidSudoku(board=board))

Solution().self_testing()