from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, v in enumerate(nums):
            hash_table[v] = i

        for i, v in enumerate(nums):
            if (target - v) in hash_table and hash_table[target-v] != i:
                return [i, hash_table[target-v]]
