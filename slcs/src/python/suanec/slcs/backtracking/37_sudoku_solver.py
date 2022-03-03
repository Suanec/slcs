# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'


# Created by enzhao on 2022/2/11.
class Solution_with_simple_backtracing(object):
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        """
        Runtime: 3552 ms, faster than 5.00% of Python3 online submissions for Sudoku Solver.
        Memory Usage: 14.5 MB, less than 38.30% of Python3 online submissions for Sudoku Solver.
        :return:
        """
        row, col = self.findUnassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True

class PositionWithCandidate(object):
    def __init__(self, _row : int, _col : int, _candidates : set):
        self.row = _row
        self.col = _col
        self.candidates = set()
        self.candidates = _candidates
        self.next_candidate_idx = 0

    @property
    def candidates_size(self):
        return len(self.candidates)

    def remove_candidate(self, _deprecated_candidate):
        if(_deprecated_candidate in self.candidates):
            self.candidates.remove(_deprecated_candidate)


class Solution(object):
    '''
    37. Sudoku Solver
    Hard

    4550

    143

    Add to List

    Share
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.



    Example 1:


    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Explanation: The input board is shown above and the only valid solution is shown below:




    Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.
    Accepted
    322,807
    Submissions
    610,895
    '''

    def related_range_of_mutex(self, row_idx, col_idx) -> (int, int):
        '''
        :param row_idx:
        :param col_idx:
        :return: matrix_row_idx, matrix_col_idx
        '''
        matrix_row_idx = int(row_idx / 3)
        matrix_col_idx = int(col_idx / 3)
        return (matrix_row_idx, matrix_col_idx)

    def solveSudoku_local(self, board):
        print(self.format_board(board=board))
        self.solveSudoku(board=board)
        print(self.format_board(board=board))

    def solveSudoku(self, board):
        return self.solveSudoku_self(board=board)

    def format_board(self, board):
        return "\n".join([ ", ".join(line) for line in board ] + ["========================="])

    def need_solver_list(self, board):
        self.need_solver_list = []

    def solveSudoku_optimize(self, board):
        pass

    def solveSudoku_self(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        total_count = 81
        value_specifed = 0
        value_specifed_bak = value_specifed
        modified = 0
        guess_flag = 0
        in_guess = False
        board_cur_bak = None
        guess_position_set = set()
        row_set_list = [set([str(x) for x in list(range(1, 10))]) for x in range(0, 9)]
        col_set_list = [set([str(x) for x in list(range(1, 10))]) for x in range(0, 9)]
        matrix_set_list = [
            [set([str(x) for x in list(range(1, 10))]) for x in range(0, 3)],
            [set([str(x) for x in list(range(1, 10))]) for x in range(0, 3)],
            [set([str(x) for x in list(range(1, 10))]) for x in range(0, 3)],
        ]
        while (value_specifed < total_count):
            modified = 0
            for row_idx in range(0, 9):
                row = board[row_idx]
                for col_idx in range(0, 9):
                    elem = row[col_idx]
                    (elem_matrix_row_idx, elem_matrix_col_idx) = \
                        self.related_range_of_mutex(row_idx=row_idx, col_idx=col_idx)
                    matrix_inner_set = matrix_set_list[elem_matrix_row_idx][elem_matrix_col_idx]
                    row_inner_set = row_set_list[row_idx]
                    col_inner_set = col_set_list[col_idx]
                    if ("." != elem):
                        remove_count = 0
                        if (elem in row_inner_set):
                            row_inner_set.remove(elem)
                            remove_count += 1
                        if (elem in col_inner_set):
                            col_inner_set.remove(elem)
                            remove_count += 1
                        if (elem in matrix_inner_set):
                            matrix_inner_set.remove(elem)
                            remove_count += 1
                        if (remove_count > 0):
                            value_specifed += 1
                            modified += 1
                    else:
                        candidates = row_set_list[row_idx].intersection(
                            col_set_list[col_idx]).intersection(
                            matrix_inner_set)
                        if (len(candidates) == 1):
                            board[row_idx][col_idx] = candidates.pop()
                        if (guess_flag > 1 and len(candidates) > 0):
                            if ((row_idx, col_idx) not in guess_position_set):
                                board[row_idx][col_idx] = candidates.pop()
                                guess_position_set.add((row_idx, col_idx))
                                guess_flag = 0
                                in_guess = True

            if (0 == modified):
                guess_flag += 1
                if (guess_flag > 1):
                    if (not board_cur_bak):
                        board_cur_bak = [[x for x in inner_row] for inner_row in board]
                        value_specifed_bak = value_specifed
                    if (in_guess):
                        for row_idx in range(0, 9):
                            for col_idx in range(0, 9):
                                board[row_idx][col_idx] = board_cur_bak[row_idx][col_idx]
                        value_specifed = value_specifed_bak
                pass

    def self_testing(self):
        board = [["7", ".", ".", ".", ".", "4", ".", "2", ","],
                 [".", "9", ".", ".", ".", ".", "3", ".", ","],
                 [".", ".", ".", ".", ".", "6", ".", ".", "8"],
                 [".", "8", ".", "9", ".", ".", ".", ".", ","],
                 [".", "3", "5", ".", ".", ".", ".", ".", "9"],
                 [".", ".", ".", ".", "7", "2", ".", "4", ","],
                 [".", ".", "9", "5", "2", ".", ".", ".", ","],
                 [".", ".", ".", ".", ".", ".", "8", "6", "7"],
                 ["1", ".", ".", "3", ".", ".", ".", ".", ","]]
        # self.solveSudoku_local(board=board)
        board = [["8", ".", "5", "4", ".", ".", "6", ".", "."],
                 ["9", ".", ".", "5", ".", ".", ".", "3", "7"],
                 ["2", "7", ".", ".", "3", "6", "4", ".", "."],
                 ["7", "6", ".", "2", ".", ".", ".", ".", "9"],
                 [".", ".", "2", "1", "6", "9", "7", "4", "."],
                 [".", ".", "9", "7", "8", ".", "2", ".", "5"],
                 ["6", ".", "7", "3", ".", ".", ".", ".", "."],
                 [".", ".", "3", ".", ".", ".", "5", ".", "6"],
                 ["1", ".", "8", ".", ".", ".", ".", "2", "."]]
        self.solveSudoku_local(board=board)
        board = [[".", "2", ".", ".", ".", "9", ".", ".", "."],
                 [".", ".", ".", "1", ".", "5", "3", ".", "2"],
                 [".", ".", "4", "2", "7", "3", ".", "1", "."],
                 ["1", "5", ".", "6", "9", "7", ".", "2", "8"],
                 ["7", "6", "8", ".", ".", ".", "1", "3", "."],
                 ["9", "4", ".", ".", "8", "1", "7", ".", "."],
                 [".", ".", ".", "7", "3", ".", "6", "5", "4"],
                 [".", "8", ".", ".", ".", ".", ".", "7", "."],
                 ["4", "3", ".", ".", "2", ".", "9", ".", "."]]
        self.solveSudoku_local(board=board)
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.solveSudoku_local(board=board)
        # from suanec.slcs.utils.list_utils import equalSeq
        # print(equalSeq([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        # ,[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        #          ))
        # self.solveSudoku(board=board)
        # print(equalSeq(board,[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]))


Solution().self_testing()
