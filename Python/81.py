# 81. Search in Rotated Sorted Array II
# Suppose an array sorted in ascending order is rotated at some pivot
#  unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search.
#  If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
from util import equal
from typing import List


def binary_search(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return True
    return False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target

        change_index = 0
        for index in range(1, len(nums)):
            if nums[index - 1] > nums[index]:
                change_index = index
                break

        if change_index:
            pivot = nums[0]
            if target >= pivot:
                return binary_search(nums[0:change_index], target)
            else:
                return binary_search(nums[change_index:], target)
        else:
            return binary_search(nums, target)


def main():
    equal(Solution().search([3, 1], 3), True)
    equal(Solution().search([1, 3], 3), True)
    equal(Solution().search([1, 1], 1), True)
    equal(Solution().search([2], 0), False)
    equal(Solution().search([], 0), False)
    equal(Solution().search([2, 5, 6, 0, 0, 1, 2], 0), True)
    equal(Solution().search([2, 5, 6, 0, 0, 1, 2], 3), False)


if __name__ == '__main__':
    main()
