# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]
from typing import List


from collections import Counter


class Solution:
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if c.get(i) == None:
                result.append(i)
        return result

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        result = []
        for i, v in enumerate(nums):
            if v > 0:
                result.append(i + 1)

        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findDisappearedNumbers)
    t.equal([5, 6], [4, 3, 2, 7, 8, 2, 3, 1])
    t = Test(s.findDisappearedNumbers_1)
    t.equal([5, 6], [4, 3, 2, 7, 8, 2, 3, 1])
