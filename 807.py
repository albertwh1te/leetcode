class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = []
        col_max = []
        for i in grid:
            row_max.append(max(i))
        print(row_max)


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.maxIncreaseKeepingSkyline)
    gridNew = [[8, 4, 8, 7],
               [7, 4, 7, 7],
               [9, 4, 8, 7],
               [3, 3, 3, 3]]
    gridOld = [[3, 0, 8, 4],
               [2, 4, 5, 7],
               [9, 2, 6, 3],
               [0, 3, 1, 0]]
    t.equal(gridNew, gridOld)
