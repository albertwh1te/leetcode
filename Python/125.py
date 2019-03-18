# 125. Valid Palindrome

# Given a string,
#  determine if it is a palindrome,
#  considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha(
            ) and not s[left].isdigit():
                left += 1
            while left < right and not s[right].isalpha(
            ) and not s[right].isdigit():
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().isPalindrome)
    t.equal(True, "A man, a plan, a canal: Panama")
    t.equal(False, "race a car")
    t.equal(False, "0P")
    t.equal(False, "ab2a")
