class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ int('0b' + ''.join(['1' for _ in range(len(bin(num)) - 2)]), 2)
