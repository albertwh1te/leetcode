# 15. 3Sum

# Given an array nums of n integers,
#  are there elements a, b, c in nums such that a + b + c = 0?
#  Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
from typing import List


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        nums.sort()  # if nums[0] > 0: # return result
        for i in range(length - 2):
            #  same as formar
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                _sum = nums[left] + nums[i] + nums[right]
                if _sum == 0:
                    result.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    # same as formar -1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # same as formar +1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == "__main__":
    from util import Test

    t = Test(Solution().threeSum)
    t.equal([[-1, -1, 2], [-1, 0, 1]], [-1, 0, 1, 2, -1, -4])
