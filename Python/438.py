# 438. Find All Anagrams in a String
# Given a string s and a non-empty string p,
#  find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and
#  the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Solution : slide window
# https: // blog.csdn.net/yy254117440/article/details/53025142
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # corner case
        if len(s) == 0 or len(p) == 0:
            return []
        result = []
        length = len(p)
        char_arr1 = [0 for _ in range(255)]
        char_arr2 = [0 for _ in range(255)]
        for i in p:
            char_arr1[ord(i)] += 1
        for i, v in enumerate(s):
            if i >= length:
                char_arr2[ord(s[i-length])] -= 1
            char_arr2[ord(v)] += 1
            if char_arr1 == char_arr2:
                result.append(i+1-length)
        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.findAnagrams)
    result = [0, 6]
    t.equal(result, "cbaebabacd", "abc")
    result = [0, 1, 2]
    t.equal(result, "abab", "ab")
