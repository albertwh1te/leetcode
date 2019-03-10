# 36. Valid Sudoku

# Determine if a 9x9 Sudoku board is valid.
#  Only the filled cells need to be validated according to
#  the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must
#  contain the digits 1-9 without repetition.

# A partially filled sudoku which is valid.

# The Sudoku board could be partially filled,
#  where empty cells are filled with the character '.'.

# Example 1:

# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:

# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1,
#  except with the 5 in the top left corner being
#     modified to 8.
#  Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:

# A Sudoku board (partially filled) could be valid
#  but is not necessarily solvable.
# Only the filled cells need to be validated according
#  to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = len(board)
        row = len(board[0])
        for i in range(column):
            check = [False for _ in range(10)]
            for j in range(row):
                if board[i][j] != ".":
                    index = ord(board[i][j])-48
                    if check[index]:
                        return False
                    check[index] = True

        for j in range(row):
            check = [False for _ in range(10)]
            for i in range(column):
                if board[i][j] != ".":
                    index = ord(board[i][j]) - 48
                    if check[index]:
                        return False
                    check[index] = True

        for i in range(row, 3):
            for j in range(column, 3):
                check = [False for _ in range(10)]
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] != ".":
                            index = ord(board[i][j]) - 48
                            if check[index]:
                                return False
                            check[index] = True
        return True
