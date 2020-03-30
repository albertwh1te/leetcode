# 279. Perfect Squares

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if i - j * j >= 0:
                    dp[i] = min(dp[i - j * j] + 1, dp[i])

        return dp[n]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.numSquares)
    t.equal(2, 2)

    t.equal(3, 12)
