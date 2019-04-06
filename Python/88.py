# 88. Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]'
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0 for _ in nums1]
        count = 0
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                result[count] = nums1[p1]
                p1 += 1
            else:
                result[count] = nums2[p2]
                p2 += 1
            count += 1

        while p1 < m:
            result[count] = nums1[p1]
            p1 += 1
            count += 1

        while p2 < n:
            result[count] = nums2[p2]
            p2 += 1
            count += 1

        for i in range(len(nums1)):
            nums1[i] = result[i]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
    nums1 = [1]
    Solution().merge(nums1, 1, [], 0)
    print(nums1)