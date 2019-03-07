# 63. Unique Paths II

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
#  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids.
#  How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

from typing import List
from util import print_matrix


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or len(obstacleGrid) == 0 or len(
                obstacleGrid[0]) == 0:
            return 0

        column = len(obstacleGrid)
        row = len(obstacleGrid[0])
        dp = [[0 for _ in range(row)] for _ in range(column)]
        dp[0][0] = 1
        for i in range(1, column):
            if obstacleGrid[i][0] != 1 and dp[i - 1][0] == 1:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for j in range(1, row):
            if obstacleGrid[0][j] != 1 and dp[0][j - 1] == 1:
                dp[0][j] = 1
            else:
                dp[0][j] = 0

        for i in range(1, column):
            for j in range(1, row):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[column - 1][row - 1]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().uniquePathsWithObstacles)
    test = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    t.equal(2, test)
    test2 = [[0, 0]]
    t.equal(1, test2)
