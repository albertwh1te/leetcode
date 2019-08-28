# 154. Find Minimum in Rotated Sorted Array II
# Suppose an array sorted in ascending order is rotated
# at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
from util import equal
from typing import List

## Origin 1,2,3,4,5,6,7

## Case1.0   3,4,5,6(mid),7,1,2

## Case1.1    3,4,5,1(mid),1,1,2

## Case2.0   7,1,2,3(mid),4,5,6

## Case3.0   7,1,1,1(mid),1,1,1


def find_min(nums: List[int], left, right):
    # length less than 2
    if (right - left) <= 1:
        return min(nums[left], nums[right])

    # nums is sorted
    if nums[left] < nums[right]:
        return nums[left]

    mid = left + ((right - left) >> 1)
    return min(find_min(nums, left, mid), find_min(nums, mid + 1, right))


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        return find_min(nums, left, right)


def main():
    equal(Solution().findMin([5, 1, 3]), 1)
    equal(Solution().findMin([1, 3, 5]), 1)
    equal(Solution().findMin([2, 2, 2, 2, 2, 0, 1]), 0)
    equal(Solution().findMin([1, 3, 3]), 1)


if __name__ == '__main__':
    main()
