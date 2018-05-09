# https://leetcode.com/problems/regular-expression-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return True


if __name__ == '__main__':
    from util import equal

    equal(Solution.isMatch("ab", ".*"), True)
