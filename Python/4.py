# 4. Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
from typing import List


class Solution:
    def find_k_th(self, nums1, nums2, k):
        """
        return the k-th in element of nums1 and nums2
        """
        # always assure len(nums1) < len(nums2)
        if len(nums1) > len(nums2):
            return self.find_k_th(nums2, nums1, k)

        # corner case
        if len(nums1) == 0:
            return nums2[k - 1]

        if (k == 1):
            return min(nums1[0], nums2[0])

        p_a = min(k / 2, len(nums1))
        p_b = k - p_a

        if a[p_a - 1] < b[p_a - 1]:
            return self.find_k_th()

        return 0

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        """
        if the length is odd  ,median is element at (length / 2 + 1)
        if the length is even ,median is the median of (length / 2) and (length / 2 + 1)
        """
        length = len(nums1) + len(nums2)
        mid = length >> 1
        mid_1 = self.find_k_th(nums1, nums2, mid + 1)
        if length % 2 != 0:
            return mid_1
        return (mid_1 + self.find_k_th(nums1, nums2, mid)) >> 1


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.findMedianSortedArrays)
    t.equal(2, [1, 2], [2])
