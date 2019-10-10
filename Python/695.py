# 695. Max Area of Island
# Given a non-empty 2D array grid of 0's and 1's,
# an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
from typing import List


class Solution:
    def infect_area(self, grid: List[List[int]], x, y) -> int:
        if x < 0 or y < 0 or y > (self.columns - 1) or x > (
                self.rows - 1) or grid[y][x] != 1:
            return 0
        area = 0
        if grid[y][x] == 1:
            grid[y][x] = 2
            area += 1
            area += self.infect_area(grid, x + 1, y)
            area += self.infect_area(grid, x - 1, y)
            area += self.infect_area(grid, x, y - 1)
            area += self.infect_area(grid, x, y + 1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        self.columns = len(grid)
        self.rows = len(grid[0])
        max_area = 0
        for y in range(self.columns):
            for x in range(self.rows):
                if grid[y][x] == 1:
                    area = self.infect_area(grid, x, y)
                    max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.maxAreaOfIsland)
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    t.equal(6, grid)
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    t.equal(0, grid)
    grid = [[]]
    t.equal(0, grid)
