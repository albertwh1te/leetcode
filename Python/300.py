# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]

# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in nums]
        dp[0] = 1
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().lengthOfLIS)
    t.equal(4, [10, 9, 2, 5, 3, 7, 101, 18])
    # t.equal()