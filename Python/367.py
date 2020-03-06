# 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false
# Accepted


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + ((right - left) >> 1)
            value = mid * mid
            if value > num:
                right = mid - 1
            elif value < num:
                left = mid + 1
            elif value == num:
                return True
        return False


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.isPerfectSquare)
    t.equal(True, 16)
    t.equal(False, 14)

