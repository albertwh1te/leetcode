# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def climbStairs_recursion(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs_recursion(n - 2) + self.climbStairs_recursion(
            n - 1)

    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().climbStairs)
    t.equal(2, 2)
    t.equal(3, 3)
