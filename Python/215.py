# 215. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
from typing import List
from heapq import heappop, heappush, heapify


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        while k > 0:
            r = heappop(nums)
            k -= 1
        return -r


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findKthLargest)
    t.equal(5, [3, 2, 1, 5, 6, 4], 2)
