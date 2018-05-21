class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.partitionLabels)
    t.equal([9, 7, 8], "ababcbacadefegdehijhklij")
