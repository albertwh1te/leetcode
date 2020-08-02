# 1535. Find the Winner of an Array Game

# Given an integer array arr of distinct integers and an integer k.

# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

# Return the integer which will win the game.

# It is guaranteed that there will be a winner of the game.

# Example 1:

# Input: arr = [2,1,3,5,4,6,7], k = 2
# Output: 5
# Explanation: Let's see the rounds of the game:
# Round |       arr       | winner | win_count
#   1   | [2,1,3,5,4,6,7] | 2      | 1
#   2   | [2,3,5,4,6,7,1] | 3      | 1
#   3   | [3,5,4,6,7,1,2] | 5      | 1
#   4   | [5,4,6,7,1,2,3] | 5      | 2
# So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
# Example 2:

# Input: arr = [3,2,1], k = 10
# Output: 3
# Explanation: 3 will win the first 10 rounds consecutively.
# Example 3:

# Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
# Output: 9
# Example 4:

# Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
# Output: 99
from typing import List

from functools import lru_cache


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        while True:
            winner = -1
            count = 0

            if arr[0] > arr[1]:
                arr[0] ,arr[1] = arr[1],arr[0]

            arr.append(arr.pop(0))
            if winner == arr[0]:
                count += 1
            else:
                winner = arr[0]
                count = 1

            if count == k:
                return winner
            if i == len(arr):
                return max(arr)
            i += 1


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.getWinner)
    t.equal(5, [2, 1, 3, 5, 4, 6, 7], 2)
    t.equal(3, [3, 2, 1], 10)
    t.equal(9, [1, 9, 8, 2, 3, 7, 6, 4, 5], 7)
    t.equal(99, [1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000)
