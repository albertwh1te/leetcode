# 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        hash_table = {}
        for char in s:
            if hash_table.get(char):
                hash_table[char] += 1
            else:
                hash_table[char] = 1

        for char in t:
            if hash_table.get(char):
                hash_table[char] -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().isAnagram)
    t.equal(True, "test", "ttes")
    t.equal(False, "rat", "ttes")
    t.equal(False, "ab", "a")
