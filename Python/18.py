#  18. 4Sum

#  Given an array nums of n integers and an integer target,
#  are there elements a, b, c, and d in nums such that a +
#  b + c + d = target? Find all unique quadruplets
#  in the array which gives the sum of target.

#  Note:

#  The solution set must not contain duplicate quadruplets.

#  Example:

#  Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

#  A solution set is:
#  [
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#  ]
from typing import List
from ast import literal_eval


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        hash_table = {}
        for index, value in enumerate(nums):
            current_target = target - value
            for i in range(index + 1, length):
                left = i + 1
                right = length - 1
                while left < right:
                    _sum = nums[left] + nums[i] + nums[right]
                    if _sum == current_target:
                        key = str(sorted([value, nums[i], nums[left], nums[right]]))
                        if key in hash_table:
                            hash_table[key] += 1
                        else:
                            hash_table[key] = 1
                        left += 1
                        right -= 1
                    elif _sum > current_target:
                        right -= 1
                    elif _sum < current_target:
                        left += 1

        results = []
        for key in hash_table:
            results.append(literal_eval(key))
        return results


if __name__ == "__main__":
    from util import Test

    t = Test(Solution().fourSum)
    t.same_elements(
        [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]], [1, 0, -1, 0, -2, 2], 0
    )
