# 456. 132 Pattern

# Given a sequence of n integers a1, a2, ..., an,
#  a 132 pattern is a subsequence ai, aj, ak
#  such that i < j < k and ai < ak < aj.
#  Design an algorithm that takes a list of n numbers as input
#  and checks whether there is a 132 pattern in the list.

# Note: n will be less than 15,000.

# Example 1:
# Input: [1, 2, 3, 4]

# Output: False

# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: [3, 1, 4, 2]

# Output: True

# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Example 3:
# Input: [-1, 3, 2, 0]

# Output: True

# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        result = 0
        # from bottom to up , value of index max to small
        max_stack = []
        # store second large value
        second_large = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_large:
                return True
            while len(max_stack) > 0 and nums[max_stack[-1]] < nums[i]:
                second_large = nums[max_stack.pop()]
            max_stack.append(i)
        return False


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.find132pattern)
    t.equal(False, [1, 2, 3, 4])
    t.equal(True, [3, 1, 4, 2])
    t.equal(True, [-1, 3, 2, 0])
    t.equal(False, [1, 0, 1, -4, -3])
    t.equal(False, [-2, 1, -2])
    t.equal(True, [3, 5, 0, 3, 4])
