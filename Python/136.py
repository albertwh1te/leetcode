# 136. Single Number

# Given a non-empty array of integers,
#  every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity.
#  Could you implement it without using extra memory?

# Example 1:

# Input: [2, 2, 1]
# Output: 1
# Example 2:

# Input: [4, 1, 2, 1, 2]
# Output: 4


from typing import List

# Concept

# If we take XOR of zero and some bit, it will return that bit
# a ^ 0 = a
# If we take XOR of two same bits, it will return 0
# a ^ a = 0
# a^b^a = (a^a)^b = b^0 = b
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

# So we can XOR all bits together to find the unique number.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Bit Manipulation
        """
        a = 0
        for i in nums:
            a = a ^ i
        return a

    def singleNumber_WithHash(self, nums: List[int]) -> int:
        """
        Hash Table
        """
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        for k, v in hash_table:
            if v == 2:
                return k
