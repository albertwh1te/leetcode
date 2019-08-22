# 922. Sort Array By Parity II
# Given an array A of non-negative integers,
# half of the integers in A are odd,
#  and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd;
# and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Note:

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
from util import equal
from typing import List


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_pointer = 0
        odd_pointer = 1
        last_index = len(A) - 1
        while ((odd_pointer <= last_index) and (even_pointer <= last_index)):
            if (A[even_pointer] & 1) != 0:
                swap(A, even_pointer, odd_pointer)
                odd_pointer += 2
            else:
                even_pointer += 2
        return A


def main():
    equal(Solution().sortArrayByParityII([0, 1]), [0, 1])
    equal(Solution().sortArrayByParityII([3, 4]), [4, 3])
    equal(Solution().sortArrayByParityII([4, 2, 5, 7]), [4, 5, 2, 7])


if __name__ == '__main__':
    main()
