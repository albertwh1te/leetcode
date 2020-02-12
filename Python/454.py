#  454. 4Sum II

#  Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

#  To make problem a bit easier,
#  all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
#  All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

#  Example:

#  Input:
#  A = [ 1, 2]
#  B = [-2,-1]
#  C = [-1, 2]
#  D = [ 0, 2]

#  Output:
#  2

#  Explanation:
#  The two tuples are:
#  1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
#  2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
from typing import List
from collections import Counter


class Solution:
    """
    Just use Minkowski addition to solve this problem
    https://en.wikipedia.org/wiki/Minkowski_addition
    """

    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        Minkowski_AB = Counter([a + b for a in A for b in B])
        Minkowski_CD = Counter([c + d for c in C for d in D])
        return sum(Minkowski_AB[ab] * Minkowski_CD[-ab] for ab in Minkowski_AB)


if __name__ == "__main__":
    from util import Test

    t = Test(Solution().fourSumCount)
    t.equal(2, [1, 2], [-2, -1], [-1, 2], [0, 2])
    t.equal(6, [-1, -1], [-1, 1], [-1, 1], [1, -1])
    t.equal(2, [1, 2], [-2, -1], [-1, 2], [0, 2])
