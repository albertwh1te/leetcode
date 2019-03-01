from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            tmp = []
            for coin in coins:
                if (i - coin) >= 0 and dp[i - coin] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount]