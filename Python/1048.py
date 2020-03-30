# 1048. Longest String Chain

# Given a list of words,
#  each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
#  For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
#  where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.

# Example 1:

# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
from typing import List


class Solution:
    def is_predecessor(self, a, b) -> int:
        # make a is always longer than b
        if len(a) < len(b):
            a, b = b, a
        has_different = False
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif has_different == False:
                i += 1
                has_different = True
            else:
                return False
        return True

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        words = sorted(words, key=lambda x: len(x))
        result = 1
        dp = [1 for _ in words] + [1]
        for i, word in enumerate(words):
            for j, word2 in enumerate(words[:i]):
                # same size  end
                if len(word) == len(word2):
                    break
                # to small
                elif len(word) - 1 > len(word2):
                    continue
                # less than one
                elif len(word) - 1 == len(word2):
                    if self.is_predecessor(word, word2):
                        dp[i] = max(dp[i], dp[j] + 1)
                        result = max(dp[i], result)
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.longestStrChain)
    t.equal(4, ["a", "b", "ba", "bca", "bda", "bdca"])
    t.equal(
        7,
        [
            "ksqvsyq",
            "ks",
            "kss",
            "czvh",
            "zczpzvdhx",
            "zczpzvh",
            "zczpzvhx",
            "zcpzvh",
            "zczvh",
            "gr",
            "grukmj",
            "ksqvsq",
            "gruj",
            "kssq",
            "ksqsq",
            "grukkmj",
            "grukj",
            "zczpzfvdhx",
            "gru",
        ],
    )
    t.equal(1, ["1", "1"])
