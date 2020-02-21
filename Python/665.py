# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        if nums[i] > nums[i+1]
            case 0: [8,6,7,10]
                i = 0,nums[i] > nums[i]:
                we change nums[i] = nums[i+1] = 6
                nums  = [6,6,7,10]
            case 1: [6,8,3,12]
                i  = 1,nums[i-1] = 6  > nums[i+1] =3
                we chanage nums[i+1] = nums[i] = 8
                nums = [6,8,8,12]
            case 2: [3,8,5,9]
                i = 1, nums[i-1] = 3 < nums[i+1] =5
                nums[i-1] = 3 > nums[i+1] = 5
                we change nums[i] = nums[i+1] = 5
                nums = [3,5,5,9]
        """
        count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if count:
                    return False
                # case 0 and case 2
                if i == 0 or nums[i - 1] < nums[i + 1]:
                    nums[i] = nums[i + 1]
                # case 1
                else:
                    nums[i + 1] = nums[i]

                count += 1
        return True


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.checkPossibility)
    t.equal(True, [1])
    t.equal(True, [4, 2, 3])
    t.equal(False, [4, 2, 1])
    t.equal(False, [3, 4, 2, 3])
    t.equal(True, [1, 4, 3])

