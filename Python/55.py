# 55. Jump Game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

from typing import List


class Solution:
    def canjump(self, position: int, nums: List[int]) -> bool:
        if position == len(nums) - 1:
            return True

        left = nums[position] if nums[position] + nums[position] < len(
            nums) - 1 else len(nums) - 1

        for i in range(position + 1, left + 1):
            if self.canjump(i, nums):
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]
        dp[len(nums) - 1] = 1
        for i in range(len(nums), -1, -1):
            diff = min(nums[i] + i, len(nums) - 1)
            for j in range(i + 1, i + diff + 2):
                if dp[j]:
                    dp[i] = 1
        return dp[0] == 1


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().canJump)
    t.equal(True, [2, 3, 1, 1, 4])
    t.equal(True, [1, 2, 3])
