# 334. Increasing Triplet Subsequence

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:

# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:

# Input: [1,2,3,4,5]
# Output: true

# Example 2:

# Input: [5,4,3,2,1]
# Output: false

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Solution:
        case 1  min1 >= nums[i]  replace min1 with nums[i]
        case 2  min1 < nums[i]  and min2 >= nums[i] replace min2 with nums[i]
        case 3  min1 < nums[i] and min2 < nums[i] found three return True
        Reason:
        ---{ case1 num[i]}--- min1 --- { case2 nums[i]} --- min2 --- { case3 nums[i]} ---
        """
        min1 = float("inf")
        min2 = float("inf")
        for num in nums:
            if min1 >= num:
                min1 = num
            elif min2 >= num:
                min2 = num
            else:
                return True
        return False