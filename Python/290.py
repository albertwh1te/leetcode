# 290. Word Pattern
# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match,
# such that there is a bijection between a letter in pattern
# and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # check if it is legal
        hash_table = dict()
        strings = str.split()
        if len(pattern) != len(strings):
            return False
        for i, v in enumerate(strings):
            if hash_table.get(pattern[i], None):
                if hash_table[pattern[i]] != v:
                    return False
            else:
                if v in hash_table.values():
                    return False
                hash_table[pattern[i]] = v
        return True


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.wordPattern)
    pattern = "aaa"
    string = "aa aa aa aa"
    t.equal(False, pattern, string)
    pattern = "abba"
    string = "dog cat cat dog"
    t.equal(True, pattern, string)
    string = "dog cat cat fish"
    t.equal(False, pattern, string)
    string = "dog dog dog dog"
    t.equal(False, pattern, string)