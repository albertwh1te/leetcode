# 1091. Shortest Path in Binary Matrix

# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
from typing import List
from queue import Queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        distance = [[-1 for _ in grid[0]] for _ in grid]
        moving_vector = [
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, 1),
            (0, -1),
        ]
        q = Queue()
        q.put((0, 0))
        if grid[0][0] == 1:
            return -1
        distance[0][0] = 1
        while q.qsize() > 0:
            (x, y) = q.get()
            if x == n and y == n:
                break
            for (v_x, v_y) in moving_vector:
                nx = x + v_x
                ny = y + v_y
                if (
                    nx <= n
                    and ny <= n
                    and nx >= 0
                    and ny >= 0
                    and grid[nx][ny] != 1
                    and distance[nx][ny] == -1
                ):
                    distance[x + v_x][y + v_y] = distance[x][y] + 1
                    q.put((x + v_x, y + v_y))
        return distance[n][n]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.shortestPathBinaryMatrix)
    t.equal(2, [[0, 1], [1, 0]])
    t.equal(4, [[0, 0, 0], [1, 1, 0], [1, 1, 0]])
    t.equal(-1, [[1, 0, 0], [1, 1, 0], [1, 1, 0]])
