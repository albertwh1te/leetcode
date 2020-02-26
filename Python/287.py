# 287. Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        result = 0
        while result != slow:
            result = nums[result]
            slow = nums[slow]
        return slow


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findDuplicate)
    t.equal(2, [1, 3, 4, 2, 2])
    t.equal(3, [3, 1, 3, 4, 2])
