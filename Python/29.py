# 29. Divide Two Integers
# Given two integers dividend and divisor,
# divide two integers without using multiplication,
# division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store
# integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # 1. zero
        # 2. sign
        # 3. too large
        if dividend == 0:
            return 0
        if divisor == 0:
            if dividend > 0:
                return 2**31 - 1
            else:
                return -1 * 2**31

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        if abs(dividend) == abs(divisor): return 1 * sign
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == 2**31 - 1:
                return -1 * 2**32
            if dividend == -1 * 2**31:
                return 2**31 - 1
            else:
                return -1 * dividend
        divisor = abs(divisor)
        dividend = abs(dividend)
        result = 0
        shift = 0

        # example  3 20
        # 3 << 0 = 3 < 20
        # 3 << 1 = 6 < 20
        # 3 << 2 = 12 < 20

        # result += 2**1
        # dividend become 10 - 6 = 4
        # 3 << 0 = 3 < 4
        # 3 << 1 = 6 > 4
        # result += 2 ** 0
        # so result is 3
        # dividend become 4 - 3 = 1
        # 3 > 1

        while divisor < dividend:
            current = divisor
            shift = 0
            while current <= dividend:
                current = divisor << shift
                shift += 1
            # we need above round result
            dividend -= (current >> 1)
            # shit should go two times because it's change of the change of current, double change!
            result += 2**(shift - 2)
        return sign * result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.divide)
    t.equal(3, 10, 3)
    t.equal(-2, 7, -3)
    t.equal(2147483647, -2147483648, -1)
    t.equal(999, -999, -1)
