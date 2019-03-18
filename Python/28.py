# 28. Implement strStr()

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string?
#  This is a great question to ask during an interview.

# For the purpose of this problem,
#  we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        while i <= (len(haystack) - len(needle)):
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
            i += 1
        return -1


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().strStr)
    t.equal(2, "hello", "ll")
    t.equal(-1, "hello", "llw")
    t.equal(4, "mississippi", "issip")
