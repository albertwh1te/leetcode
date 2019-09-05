# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of
# the 9 3x3 sub-boxes of the grid.

# Empty cells are indicated by the character '.'.

# ...and its solution numbers marked in red.

# Note:

# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.

# The given board size is always 9x9.

from util import equal
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)

    def helper(self, board, x, y):
        """
        case 1: reach the last row, end of recursion
        case 2: reach the last column, go next row
        case 3: check if the the value is validated, if true,
        check x + 1  , if true return the value 
        else: retore  the board
        """
        if y == len(board):
            return True
        if x >= len(board[0]):
            return self.helper(board, 0, y + 1)
        if board[y][x] == '.':
            for n in range(1, 10):
                n = str(n)
                if self.validate(board, x, y, n):
                    board[y][x] = n
                    if self.helper(board, x + 1, y):
                        return True
                    board[y][x] = "."
            return False
        else:
            return self.helper(board, x + 1, y)

    def validate(self, board, x, y, value):
        for row in range(len(board)):
            if board[row][x] == value:
                return False

        for column in range(len(board[0])):
            if board[y][column] == value:
                return False

        row = y - y % 3
        column = x - x % 3
        for i in range(3):
            for j in range(3):
                if board[row + i][column + j] == value:
                    return False
        return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(board)
    expected_board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                      ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                      ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                      ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                      ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                      ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                      ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                      ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                      ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
    equal(board, expected_board)


if __name__ == '__main__':
    main()