class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = sorted(nums)
        return new[::2]


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().arrayPairSum)
    t.equal(4, [1, 4, 3, 2])
