# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        frequent = dict()
        for num in nums:
            if num in frequent:
                frequent[num] += 1
            else:
                frequent[num] = 0

        for key, value in frequent.items():
            heappush(max_heap, (-value, key))

        result = []
        for n in range(k):
            result.append(heappop(max_heap)[1])
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()

    t = Test(s.topKFrequent)
    t.equal([1, 2], [1, 1, 1, 2, 2, 3], 2)
    t.equal([1, 2, 3], [1, 1, 1, 2, 2, 3], 3)
    t.equal([1], [1], 1)
    t.equal([-1, 2], [4, 1, -1, 2, -1, 2, 3], 2)
