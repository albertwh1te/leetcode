# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2]
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

from util import equal
from typing import List

## Original Array : 1,2,3,4,5,6,7

## CASE 1:  6 7 1 2(mid) 3 4 5

## CASE 1 mid < end ,nums[mid:end] is sorted  minium is in nums[start,mid]

## CASE 2:  3 4 5 6(mid) 7 1 2

## CASE 2 mid >= end, nums[start: mid] is sorted minum is in nums[mid+1,end]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[mid]


def main():
    equal(Solution().findMin([3, 4, 5, 1, 2]), 1)
    equal(Solution().findMin([4, 5, 6, 7, 0, 1, 2]), 0)


if __name__ == '__main__':
    main()
