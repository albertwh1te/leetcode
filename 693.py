class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return "0" not in bin(n ^ (n << 1))[1:-1]


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.hasAlternatingBits)
    t.equal(True, 5)
    t.equal(False, 7)
    t.equal(False, 11)
    t.equal(True, 10)
    t.equal(True, 42)
