# 518. Coin Change 2


# You are given coins of different denominations and a total amount of money.
#  Write a function to compute the number of combinations that make up that amount.
#  You may assume that you have infinite number of each kind of coin.


# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        numbers = [0 for _ in range(amount + 1)]
        numbers[0] = 1
        for coin in coins:
            for n in range(coin, amount + 1):
                if n - coin >= 0:
                    numbers[n] += numbers[n - coin]
        return numbers[amount]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.change)
    t.equal(2, 3, [1, 2, 5])
    t.equal(4, 5, [1, 2, 5])
    t.equal(0, 3, [2])
    t.equal(1, 10, [10])
