# 213. House Robber II

# You are a professional robber planning to rob houses along a street.
#  Each house has a certain amount of money stashed.
#  All houses at this place are arranged in a circle.
#  That means the first house is the neighbor of the last one.
#  Meanwhile, adjacent houses have security system connected
#  and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
#  determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.1
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        if len(nums) == 3:
            return nums[1]
        return max(self.rob1(nums[1:]), nums[-1] + self.rob1(nums[:-1]))

    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in nums]
        dp[len(nums) - 1] = nums[-1]
        dp[len(nums) - 2] = nums[-1] if nums[-2] < nums[-1] else nums[-2]
        for i in range(len(nums) - 3, -1, -1):
            v1 = nums[i] + dp[i + 2]
            v2 = dp[i + 1]
            dp[i] = max(v1, v2)
        return dp[0]
