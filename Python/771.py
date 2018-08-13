class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([{x: 1 for x in J}.get(x, 0) for x in S])


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.numJewelsInStones)
    t.equal(3, "aA", "aAAbbbb")
    t.equal(0, "z", "ZZ")
