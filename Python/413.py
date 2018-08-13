class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        result = 0
        slices_num = 0
        for i in range(len(A) - 2):
            if A[i] - A[i + 1] == A[i + 1] - A[i + 2]:
                slices_num += 1
                result += slices_num
            else:
                slices_num = 0
        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.numberOfArithmeticSlices)
    t.equal(3, [1, 2, 3, 4])
    t.equal(10, [1, 2, 3, 4, 5, 6])
    t.equal(2, [1, 2, 3, 8, 9, 10])
