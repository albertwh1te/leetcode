# 416. Partition Equal Subset Sum

# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.


# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].


# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        """
        _sum = sum(nums)
        if (_sum & 1) == 1:
            return False
        dp = [0 for _ in range(_sum + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(_sum, 0, -1):
                if j >= num:
                    dp[j] = dp[j - num] or dp[j]
                if dp[_sum >> 1] == 1:
                    return True
        return False

    def canPartition_2D_DP(self, nums: List[int]) -> bool:
        """
        dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        """
        _sum = sum(nums)
        if (_sum & 1) == 1:
            return False

        length = len(nums) - 1
        dp = [[0 for _ in range(_sum + 1)] for _ in range(length + 1)]

        dp[0][0] = True

        for i in range(1, length + 1):
            dp[i][0] = True

        for j in range(1, _sum + 1):
            dp[0][j] = False

        for j in range(1, _sum + 1):
            for i in range(1, length + 1):
                dp[i][j] = (
                    dp[i - 1][j] or dp[i - 1][j - nums[i]]
                    if j >= nums[i]
                    else dp[i - 1][j]
                )

        return dp[length][_sum // 2]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.canPartition)
    t.equal(True, [23, 13, 11, 7, 6, 5, 5])
    t.equal(False, [2, 2, 3, 5])
    t.equal(True, [1, 5, 11, 5])
    t.equal(False, [1, 2, 3, 5])
