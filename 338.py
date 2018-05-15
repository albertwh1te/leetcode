class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = list(map(lambda x: bin(x).count(
            '1'), (i for i in range(num + 1))))
        return result
