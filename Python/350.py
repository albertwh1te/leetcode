# 350. Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2, 2]
# Example 2:

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
# Note:

# Each element in the result should appear as many times as it shows in both
#  arrays.
# The result can be in any order.
# Follow up:

# What if the given array is already sorted?
#  How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size?
#  Which algorithm is better?
# What if elements of nums2 are stored on disk,
#  and the memory is limited such that you cannot load all elements
#  into the memory at once

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums2[p2] > nums1[p1]:
                p1 += 1
        return result
