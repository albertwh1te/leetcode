# 877. Stone Game
# lex and Lee play a game with piles of stones.
#   There are an even number of piles arranged in a row,
#  and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones.
#   The total number of stones is odd, so there are no ties.

# Alex and Lee take turns,
#  with Alex starting first.
#  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.

#  This continues until there are no more piles left,

#  at which point the person with the most stones wins.

# Assuming Alex and Lee play optimally,
#  return True if and only if Alex wins the game.

# Example 1:

# Input: [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

# Note:

# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
from typing import List


class Solution:
    # Mathematics will always prevail!
    # Alex clearly always wins the 2 pile game. With some effort, we can see that she always wins the 4 pile game.

    # If Alex takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. At least one of first + third, second + fourth is larger, so she can always win.

    # We can extend this idea to N piles. Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black. Alex can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.

    # Hence, Alex always wins the game.
    def stoneGame(self, piles: List[int]) -> bool:
        return True