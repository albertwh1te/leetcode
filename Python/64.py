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
            r = grid[x][y] + min(
                self.minPathSumHelper(grid, x, y - 1),
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

    def minPathSum2(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for i in range(len(grid[0]) - 2, 0, -1):
            dp[i][-1] = dp[i - 1][-1] + grid[i][-1]
        for j in range(len(grid) - 2, 0, -1):
            dp[-1][j] = dp[-1][j - 1] + grid[-1][j]
        from util import print_matrix
        print_matrix(dp)
        print_matrix(grid)
        return dp[0][0]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().minPathSum2)
    test = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    t.equal(7, test)
