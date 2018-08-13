class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if n > k:
            return [i + [n] for i in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
        else:
            return [i + [n] for i in self.combine(n - 1, k - 1)]


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.combine)
    RESULT = [[1, 4], [2, 4], [3, 4], [1, 3], [2, 3], [1, 2]]
    t.equal(RESULT, 4, 2)
