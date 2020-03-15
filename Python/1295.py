# 1295. Find Numbers with Even Number of Digits

# Given an array nums of integers, return how many of them contain an even number of digits.


# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.


# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

from typing import List


class Solution:
    def digits(self, num: int) -> int:
        result = 0
        while num > 0:
            num //= 10
            result += 1
        return result

    def findNumbers2(self, nums: List[int]) -> int:
        return sum(1 for _ in filter(lambda x: self.digits(x) % 2 == 0, nums))

    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for i in nums if len(str(i)) % 2 == 0)


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findNumbers)
    t.equal(2, [12, 345, 2, 6, 7896])
    t.equal(1, [555, 901, 482, 1771])

