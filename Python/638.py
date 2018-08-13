import operator


class Solution:
    def hasBelowZero(self, array):
        for i in array:
            if i < 0:
                return True
        return False

    def mulList(self, a, b):
        return map(operator.mul, a, b)

    def subtractList(self, a, b):
        return list(map(operator.sub, a, b))

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        results = []
        for s in special:
            remains = self.subtractList(needs, s[:-1])
            lazysolution = sum(self.mulList(needs, price))
            if not self.hasBelowZero(remains):
                results.append(
                    min(s[-1] + self.shoppingOffers(price, special, remains), lazysolution))
            else:
                results.append(lazysolution)
        return min(results)


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.shoppingOffers)
    t.equal(14, [2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2])
    t.equal(11, [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1])
