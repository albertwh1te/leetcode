# 33. Search in Rotated Sorted Array

# Suppose an array sorted in ascending order
# is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search.
#  If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
from util import equal
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid
            # nums[left:mid] is sorted
            elif nums[mid] >= nums[left]:
                # target in [left,mid)
                if nums[mid] > target and nums[left] <= target:
                    flag = binary_search(nums[left:mid], target)
                    return left + flag if flag != -1 else flag

                else:
                    left = mid + 1
            # nums[mid:right+1] is sorted
            elif nums[mid] < nums[left]:
                # target in [mid,right+1)
                if nums[mid] <= target and nums[right] >= target:
                    flag = binary_search(nums[mid:right + 1], target)
                    return mid + flag if flag != -1 else flag
                else:
                    right = mid - 1
        return -1


# Solution:
# Origin: 1,2,3,4,5,6,7
# Case 1: 3,4,5,6,7,1,2
# Case 2: 7,1,2,3,4,5,6


def main():
    equal(Solution().search([4, 5, 6, 7, 0, 1, 2], 6), 2)
    equal(Solution().search([4, 5, 6, 7, 0, 1, 2], 4), 0)
    equal(Solution().search([4, 5, 6, 7, 0, 1, 2], 2), 6)
    equal(Solution().search([4, 5, 6, 7, 0, 1, 2], 3), -1)
    equal(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)
    equal(Solution().search([5, 1, 3], 2), -1)
    equal(Solution().search([5, 1, 3], 3), 2)


if __name__ == '__main__':
    main()
