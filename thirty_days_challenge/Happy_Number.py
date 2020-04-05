#  Happy Number

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.next_number(n)
        fast = self.next_number(self.next_number(n))
        while fast != slow:
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))
        return slow == 1

    def next_number(self, n: int) -> int:
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n //= 10
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.isHappy)
    t.equal(True, 19)
    t.equal(False, 11)
