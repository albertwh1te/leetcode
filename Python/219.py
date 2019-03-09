# 219. Contains Duplicate II
# Given an array of integers and an integer k,
#  find out whether there are two distinct indices
#  i and j in the array such that nums[i] = nums[j]
#  and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1, 2, 3, 1], k = 3
# Output: true
# Example 2:

# Input: nums = [1, 0, 1, 1], k = 1
# Output: true
# Example 3:

# Input: nums = [1, 2, 3, 1, 2, 3], k = 2
# Output: false
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, v in enumerate(nums):
            if hash_table.get(v, -1) != -1:
                if(i - hash_table[v]) <= k:
                    return True
            hash_table[v] = i
        return False
