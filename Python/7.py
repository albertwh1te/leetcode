# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit
#  signed integer range: [−231,  231 − 1]. For the purpose of this problem,
#  assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x != 0:
            print(x, "))", result)
            result = result * 10 + x % 10
            if abs(result) > (2**31 - 1):
                return 0
            x = x // 10
        return result


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().reverse)
    # t.equal(321, 123)
    t.equal(-321, -123)
    # t.equal(0, 1534236469)
    # t.equal(0, 1563847412)
