# 46. Permutations
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List


class Solution:
    def help(self, index: int) -> [int]:
        if index == 0:
            return [[n] for n in self.nums]
        results = []
        for num in self.nums:
            for result in self.help(index-1):
                if num not in result:
                    results.append([num]+result)
        return results

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        return self.help(len(nums) - 1)


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.permute)
    results = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    t.same_elements(
        results, [1, 2, 3]
    )
