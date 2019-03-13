# 49. Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
from typing import List, Tuple
from string import ascii_lowercase


def string2count(raw: str) -> Tuple[int]:
    """
    convert string to tuple Int
    """
    count = [0 for _ in range(26)]
    for s in raw:
        count[ord(s) - ord('a')] += 1
    return tuple(count)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        keys = []
        for s in strs:
            key = string2count(s)
            if key in keys:
                result[keys.index(key)].append(s)
            else:
                keys.append(key)
                result.append([s])
        return result


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().groupAnagrams)
    t.equal([], ["eat", "tea", "tan", "ate", "nat", "bat"])
