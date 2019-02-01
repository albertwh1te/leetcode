# https://leetcode.com/problems/regular-expression-matching/description/
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        state = [[0 for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        state[0][0] = 1
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                if i >= 2:
                    state[0][i] = state[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    state[i][j] = state[i - 1][j - 1]
                elif p[j - 1] == '*':
                    state[i][j] = state[i][j - 1] or state[i][j - 2] or (
                        state[i - 1][j] and
                        (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    state[i][j] = state[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return state[len(s)][len(p)] == 1


if __name__ == '__main__':
    from util import equal
    t = Solution()
    print('start')
    equal(t.isMatch("", "a"), False)
    equal(t.isMatch("aa", ""), False)
    equal(t.isMatch("aa", "a"), False)
    equal(t.isMatch("aa", "a*"), True)
    equal(t.isMatch("a", "ab*a"), True)
    equal(t.isMatch("aab", "c*a*b"), True)
    equal(t.isMatch("mississippi", "mis*is*p*."), False)
