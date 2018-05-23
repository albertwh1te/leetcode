class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        results = (a ^ b) % 0x100000000

        carry = ((a & b) << 1) % 0x100000000
        if carry != 0:
            return self.getSum(results, carry)
        return results


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().getSum)
    t.equal(3, 1, 2)
    t.equal(1, -1, 2)
    t.equal(-3, -1, -2)
    t.equal(30, 10, 20)
    t.equal(10001, 10000, 1)
    t.equal(443, 331, 112)
