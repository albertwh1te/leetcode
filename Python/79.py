# 79. Word Search # Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false
from util import equal
from typing import List


def word_search(board: List[List[str]], word: str, current_index: int,
                current_x: int, current_y: int, path: List[int]) -> bool:
    last_row = len(board) - 1
    last_colum = len(board[0]) - 1
    if current_y > last_row or current_x > last_colum or current_y < 0 or current_x < 0:
        return False
    last_index = len(word) - 1
    # Base Case last index
    if current_index == last_index and (current_y, current_x) not in path:
        return board[current_y][current_x] == word[last_index]
    if word[current_index] == board[current_y][current_x] and (
            current_y, current_x) not in path:
        new_path = path + [(current_y, current_x)]
        return word_search(board, word,current_index+1,current_x+1,current_y,new_path)\
        or word_search(board, word,current_index+1,current_x-1,current_y,new_path)\
        or word_search(board, word,current_index+1,current_x,current_y+1,new_path)\
        or word_search(board, word,current_index+1,current_x,current_y-1,new_path)
    else:
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        colums = len(board[0])
        result = False
        for y in range(rows):
            for x in range(colums):
                result |= word_search(board, word, 0, x, y, [])
        return result


def main():
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    equal(Solution().exist(board, word), True)

    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "SEE"
    equal(Solution().exist(board, word), True)

    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCB"
    equal(Solution().exist(board, word), False)

    board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"],
             ["a", "b", "a", "a", "a", "b"], ["a", "b", "a", "b", "b", "a"],
             ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
             ["a", "a", "b", "a", "a", "b"]]
    word = "aabbbbabbaababaaaabababbaaba"
    equal(Solution().exist(board, word), True)

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    equal(Solution().exist(board, word), True)


if __name__ == '__main__':
    main()
