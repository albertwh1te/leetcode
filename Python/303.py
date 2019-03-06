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


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}

    def sumRange(self, i: int, j: int) -> int:
        hit = self.cache.get((i, j))
        if hit:
            return hit
        r = sum(self.nums[i:j + 1])
        self.cache[(i, j)] = r
        return r


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)