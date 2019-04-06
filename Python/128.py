# 128. Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# HashSet and Intelligent Sequence Building
# Intuition

# It turns out that our initial brute force solution was on the right track,
#  but missing a few optimizations necessary to reach O(n) time complexity.

# Algorithm

# This optimized algorithm contains only two changes from the brute force approach:
#  the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups,
#  and we only attempt to build sequences from numbers that are not already part of a longer sequence.
#  This is accomplished by first ensuring that the number that would immediately precede
# the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.

from typing import List


class Solution:
    def bruteforce(self, nums: List[int]) -> int:
        max_length = 0
        for num in nums:
            current_length = 1
            while (num + 1) in nums:
                num += 1
                current_length += 1
            max_length = max(current_length, max_length)
        return max_length

    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique = set(nums)
        for num in unique:
            # we only want head so we do not build from nums that already in sequence
            # O(1)
            if num - 1 not in unique:
                current_length = 1
                while (num + 1) in unique:
                    num += 1
                    current_length += 1
                max_length = max(current_length, max_length)
        return max_length


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().longestConsecutive)
    t.equal(4, [100, 4, 200, 1, 3, 2])
