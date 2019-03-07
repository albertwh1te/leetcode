# 152. Maximum Product Subarray

# Given an integer array nums,
#  find the contiguous subarray within an array (containing at least one number)
# which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for i in nums]
        dp_min = [0 for i in nums]
        dp_min[0], dp_max[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1],
                            nums[i])
            dp_min[i] = min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1],
                            nums[i])
        return max(dp_max)


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().maxProduct)
    t.equal(6, [2, 3, -2, 4])
    t.equal(0, [-2, 0, -1])
    t.equal(2, [0, 2])
    t.equal(24, [-2, 3, -4])
