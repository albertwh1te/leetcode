# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement,
#  where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        We place queens on the board one row at a time,
        starting with the top row. To place the rth queen, we methodically try all n squares in
        row r from left to right in a simple for loop. If a particular square is attacked by
        an earlier queen, we ignore that square; otherwise, we tentatively place a queen
        on that square and recursively grope for consistent placements of the queens in
        later rows
        """
        results = []

        Q = [-1 for _ in range(n)]

        def Place_Queens(Q: List[int], r: int):
            if r == len(Q):
                result = []
                # Q = [""]
                for i in Q:
                    result.append("".join(
                        ["." if x != i else "Q" for x in range(n)]))
                results.append(result)
            else:
                for j in range(len(Q)):
                    legal = True
                    for i in range(r):
                        if ((Q[i] == j) or (Q[i] == j + r - i)
                                or (Q[i] == j - r + i)):
                            legal = False
                    if (legal):
                        Q[r] = j
                        Place_Queens(Q, r + 1)

        Place_Queens(Q, 0)

        return results


if __name__ == '__main__':
    from util import Test
    s = Solution()
    result = [[".Q..", "...Q", "Q...", "..Q."],
              ["..Q.", "Q...", "...Q", ".Q.."]]
    t = Test(s.solveNQueens)
    t.equal(result, 4)
