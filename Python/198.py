# 198. House Robber
# You are a professional robber planning to rob houses along a street.
#  Each house has a certain amount of money stashed,
#  the only constraint stopping you from robbing each of them is that
#  adjacent houses have security system connected
#  and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
#  determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List


class Solution:
    def rob_helper(self, nums, i):
        if i < len(nums) - 1:
            return 0
        if i == len(nums) - 1:
            return nums[i]
        v1 = nums[i] + self.rob_helper(nums, i + 2)
        v2 = self.rob_helper(nums, i + 1)
        return max(v1, v2)

    def rob_recursion(self, nums: List[int]) -> int:
        return self.rob_helper(nums, 0)

    def rob(self, nums: List[int]) -> int:
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


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().rob)
    t.equal(4, [2, 1, 1, 2])
