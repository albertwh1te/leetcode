# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        times = [0 for i in range(26)]
        for char in s:
            times[ord(char) - ord('a')] += 1
        for i, v in enumerate(s):
            if times[ord(v) - ord('a')] == 1:
                return i
        return -1


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().firstUniqChar)
    t.equal(0, "leetcode")
    t.equal(2, "loveleetcode")
    t.equal(-1, "aaaaa")
