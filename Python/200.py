# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water),
#  count the number of islands.
#  An island is surrounded by water and is formed by connecting adjacent lands
#  horizontally or vertically.
#  You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3
from typing import List


class Solution:
    def infect(self, grid: List[List[str]], x: int, y: int):
        if x >= len(grid) or y >= len(
                grid[0]) or x < 0 or y < 0 or grid[x][y] != "1":
            return
        else:
            grid[x][y] = "2"
            self.infect(grid, x - 1, y)
            self.infect(grid, x, y - 1)
            self.infect(grid, x + 1, y)
            self.infect(grid, x, y + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number += 1
                    self.infect(grid, i, j)
        return number


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().numIslands)
    t.equal(3, [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
    t.equal(3, [["1", "0", "1", "1", "0", "1", "1"]])