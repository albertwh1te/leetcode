# 303. Range Sum Query - Immutable

# Given an integer array nums,
#  find the sum of the elements between indices i and j (i ≤ j),
#  inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]


if __name__ == "__main__":
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print(n.sumRange(0, 2) == 1)
    print(n.sumRange(2, 5) == -1)
    print(n.sumRange(0, 5) == -3)

