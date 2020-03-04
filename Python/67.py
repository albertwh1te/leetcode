# 67. Add Binary

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        while i >= 0 and j >= 0:
            _sum = carry
            _sum += ord(a[i]) + ord(b[j]) - 2 * ord("0")
            result += str(_sum % 2)
            carry = _sum >> 1

            i -= 1
            j -= 1

        while i >= 0:
            _sum = carry
            _sum += ord(a[i]) - ord("0")
            result += str(_sum % 2)
            carry = _sum >> 1
            i -= 1

        if carry == 1:
            result += "1"

        return result[::-1]


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.addBinary)
    t.equal("100", "11", "1")
    t.equal("10101", "1010", "1011")
    t.equal("0", "0", "0")
