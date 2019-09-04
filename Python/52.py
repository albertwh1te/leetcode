# 52. N-Queens II

# Share The n-queens puzzle is the problem of placing
# n queens on an n×n chessboard such that
# no two queens attack each other.

# Given an integer n,
# return the number of distinct solutions to the n-queens puzzle.

# Example:

# Input: 4
# Output: 2
# Explanation: There are two distinct solutions
# to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
from util import equal
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def place_queen(table: List[int], row: int):
            result = 0
            if row == len(table):
                return 1
            else:
                for x in range(len(table)):
                    legal = True
                    for y in range(row):
                        if (
                                # horizontally
                                table[y] == x or
                                # right diagonal
                                table[y] == x + (row - y) or
                                # left diagonal
                                table[y] == x - (row - y)):
                            legal = False
                    if legal:
                        table[row] = x
                        result += place_queen(table, row + 1)
            return result

        table = [-1 for i in range(n)]
        return place_queen(table, 0)


def main():
    equal(Solution().totalNQueens(4), 2)


if __name__ == '__main__':
    main()
