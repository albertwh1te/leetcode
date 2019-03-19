# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        answer = ""
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) <= i or s[i] != strs[0][i]:
                    return answer
            answer = answer + strs[0][i]
        return answer


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().longestCommonPrefix)
    t.equal("fl", ["flower", "flow", "flight"])
    t.equal("", ["dog", "racecar", "car"])
