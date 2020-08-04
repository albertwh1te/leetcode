# 342. Power of Four
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 4:
            return num == 1
        from math import log
        power = round(log(num,4))
        return 4 ** power == num

if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.isPowerOfFour)
    t.equal(True,16)
    t.equal(False,5)
