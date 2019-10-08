# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O),
# capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's
# into 'X's in that surrounded region.

# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border,
# which means that any 'O' on the border of
# the board are not flipped to 'X'.
# Any 'O' that is not on the border and
# it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally
# or vertically.
from typing import List


class Solution:
    def helper(self, x, y, board):
        if x < 0 or y < 0 or y >= self.columns or x >= self.rows:
            return
        if board[y][x] == "O":
            board[y][x] = "$"
            self.helper(x - 1, y, board)
            self.helper(x + 1, y, board)
            self.helper(x, y + 1, board)
            self.helper(x, y - 1, board)

    def preprocess(self, board):
        for x in range(self.rows):
            self.helper(x, 0, board)
            self.helper(x, self.columns - 1, board)
        for y in range(self.columns):
            self.helper(0, y, board)
            self.helper(self.rows - 1, y, board)

    def process(self, board):
        for y in range(self.columns):
            for x in range(self.rows):
                if board[y][x] == "$":
                    board[y][x] = "O"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.columns = len(board)
        self.rows = len(board[0])
        self.preprocess(board)
        for y in range(self.columns):
            for x in range(self.rows):
                if board[y][x] == "O":
                    board[y][x] = "X"
        self.process(board)


if __name__ == '__main__':
    from util import Test
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
                ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    t = Test(s.solve)
    t.equal(None, board)
    print(board)
    assert board == expected
