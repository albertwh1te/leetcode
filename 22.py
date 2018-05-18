class Solution:
    def generateParenthesisHelper(self, left, right, string):
        if left == 0 and right == 0:
            self.results.append(string)
            return
        if left > 0:
            self.generateParenthesisHelper(
                left - 1, right, string + "(")
        if right > left:
            self.generateParenthesisHelper(
                left, right - 1, string + ")")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.results = []
        self.generateParenthesisHelper(n, n, "")
        return sorted(set(self.results))


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.generateParenthesis)
    result = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    t.equal(result, 3)
