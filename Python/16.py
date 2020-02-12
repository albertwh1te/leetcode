from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float("inf")
        length = len(nums)
        nums.sort()
        result = 0
        for i in range(length - 1):
            left = i + 1
            right = length - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                diff = target - _sum
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = _sum
                #  the sum is less than target, move left to right
                if diff > 0:
                    left += 1
                # the  sum is great than target, move right point to left
                elif diff < 0:
                    right -= 1
                # if the diff is zero ,we can try another value
                else:
                    break
        return result


if __name__ == "__main__":
    from util import Test

    t = Test(Solution().threeSumClosest)
    t.equal(2, [-1, 2, 1, -4], 1)
    t.equal(0, [0, 2, 1, -3], 1)
    t.equal(3, [0, 1, 2], 3)
    t.equal(-1, [1, 1, -1, -1, 3], -1)
