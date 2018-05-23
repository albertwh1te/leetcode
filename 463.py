class Solution(object):
    def checkandmove(self, island_dict, key):
        if island_dict.get(key):
            return 1
        return 0

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        raw = sum(sum(i) for i in grid) * 4
        island_dict = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island_dict[(i, j)] = 1
        for k in island_dict:
            if island_dict.get(((k[0] + 1), k[1])):
                raw = raw - 2
            if island_dict.get((k[0], (k[1] + 1))):
                raw = raw - 2
        return raw


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().islandPerimeter)

    input1 = [[0, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 0, 0],
              [1, 1, 0, 0]]
    t.equal(16, input1)
