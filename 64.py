class Solution:
    def minPathSumHelper(self, grid, x, y):
        if self.cache.get((x, y)):
            r = self.cache.get((x, y))
        elif x == 0 and y == 0:
            r = grid[x][y]
        elif x == 0:
            distance = self.minPathSumHelper(grid, x, y - 1)
            r = grid[x][y] + distance
        elif y == 0:
            distance = self.minPathSumHelper(grid, x - 1, y)
            r = grid[x][y] + distance
        else:
            r = grid[x][y] + min(self.minPathSumHelper(grid, x, y - 1),
                                 self.minPathSumHelper(grid, x - 1, y))
        self.cache[(x, y)] = r
        return r

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.cache = {}
        x = len(grid) - 1
        y = len(grid[0]) - 1
        return self.minPathSumHelper(grid, x, y)


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().minPathSum)
    input = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    input2 = [[7, 0, 8, 8, 0, 3, 5, 8, 5, 4], [4, 1, 2, 9,
                                               9, 6, 0, 8, 6, 9], [9, 7, 1, 1, 0, 1, 2, 4, 1, 7]]
    t.equal(7, input)
    t.equal(13, input2)
