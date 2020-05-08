# 581. Shortest Unsorted Continuous Subarray

# Given an integer array,
# you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        1. find the minimum
        2. find the maximum
        3. find the start
        4. find the end
        5. return the result 
        """
        length = len(nums)
        unsorted = False

        minimum = float("inf")
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                unsorted = True
            if unsorted:
                minimum = min(nums[i], minimum)

        unsorted = False
        maximum = float("-inf")
        for i in range(length - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                unsorted = True
            if unsorted:
                maximum = max(nums[i - 1], maximum)

        start, end = 0, 0

        for i in range(length):
            if nums[i] > minimum:
                start = i
                break

        for i in range(length - 1, -1, -1):
            if nums[i] < maximum:
                end = i
                break
        return 0 if end == start else end - start + 1


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findUnsortedSubarray)
    t.equal(5, [2, 6, 4, 8, 10, 9, 15])
    t.equal(4, [1, 3, 2, 2, 2])
    t.equal(0, [1, 2, 3, 4])
    t.equal(2, [2, 1])
