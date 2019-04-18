# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Algorithm

# The naive approach is very straightforward. But it is too slow. So how can we optimize it?

# In the naive approaches,
#  we repeatedly check a substring to see if it has duplicate character.
#  But it is unnecessary. If a substring s_{ij}s
# ij
# ​
#  from index ii to j - 1j−1 is already checked to have no duplicate characters.
#  We only need to check if s[j]s[j] is already in the substring s_{ij}s
# ij
# ​
#  .

# To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2)O(n
# 2
#  ) algorithm. But we can do better.

# Solution:k
# For i in s, we just need return the maxvalue of all Longest Substring that start at i.


class Solution:
    def lengthOfLongestSubstring_with_hashtable(self, s: str) -> int:
        length = len(s)
        answer, left, right = 0, 0, 0
        chars = set()
        while left < length and right < length:
            if s[left] in chars:
                chars.remove(s[right])
                right += 1
            else:
                chars.add(s[left])
                left += 1
                answer = max(answer, left - right)
        return answer

    def lengthOfLongestSubstring(self, s: str) -> str:
        '''
        The above solution requires at most 2n steps.
        In fact, it could be optimized to require only n steps.
        Instead of using a set to tell if a character exists or not,
        we could define a mapping of the characters to its index.
        Then we can skip the characters immediately when we found a repeated character.
        '''
        length = len(s)
        answer, left, right = 0, 0, 0
        # 128 for ascii
        index = [0 for i in range(128)]
        while right < length:
            if index[ord(s[right])]:
                left = max(index[ord(s[right])], left)
            index[ord(s[right])] = right + 1
            right += 1
            answer = max(answer, right - left)
        return answer