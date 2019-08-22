# 905. Sort Array By Parity
# Given an array A of non-negative integers,
# return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
from typing import List
from util import equal


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        while left < right:
            if (A[left] & 1) == 0:
                left += 1
            else:
                swap(A, left, right)
                right -= 1
        return A


def main():
    equal(Solution().sortArrayByParity([0, 1]), [0, 1])
    equal(Solution().sortArrayByParity([3, 1, 2, 4]), [4, 2, 1, 3])


if __name__ == '__main__':
    main()
