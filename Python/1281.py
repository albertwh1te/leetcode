class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        _sum = 0
        for i in str(n):
            product *= int(i)
            _sum += int(i)
        return product - _sum
