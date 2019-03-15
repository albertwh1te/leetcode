# 5. Longest Palindromic Substring

# Given a string s,
# find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        To improve over the brute force solution,
        we first observe how we can avoid unnecessary re-computation while validating palindromes.
        Consider the case "ababa".
        If we already knew that "bab" is a palindrome,
        it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.
        We define P(i,j)P(i,j) as following:
        P[i,j] = 1  if i ==j
        =  S[i] ==S[j]   if j = i+1
        =  S[i] == S[j] && P[i+1][j-1]  if j>i+1
        p(0,0) = True
        '''
        if len(s) == 0:
            return s
        length = len(s)
        max_length = 0
        start = 0
        end = 0
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) and ((i - j < 2) or dp[j + 1][i - 1])
                if dp[j][i] and max_length < (i - j + 1):
                    max_length = i - j + 1
                    start = j
                    end = i
            dp[i][i] = True
        return s[start:end + 1]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().longestPalindrome)
    t.equal("bab", "babad")
    t.equal("a", "abcda")
    t.equal("a", "ac")
    t.equal("a", "a")
    t.equal("aaaa", "aaaa")