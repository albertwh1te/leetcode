# 326. Power of Three
# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?


# Solution:

# log3n = log10n / log103

# the reason we use log10

# log(243, 3) simply doesn't give you exactly 5:
# https: // stackoverflow.com/questions/35139107/weird-behaviour-for-python-is-integer-from-floor

# >> > '%.60f' % log(243, 3)
# '4.999999999999999111821580299874767661094665527343750000000000'
# As the docs say, log(x, base) is "calculated as log(x)/log(base)".
#  And neither log(243) nor log(3) can be represented exactly,
#  and you get rounding errors.
#  Sometimes you're lucky, sometimes you're not. Don't count on it.


from math import log10


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (log10(n)/log10(3)).is_integer()
