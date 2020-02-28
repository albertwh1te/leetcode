# 1122. Relative Sort Array

# Given two arrays arr1 and arr2,
#  the elements of arr2 are distinct,
#  and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items
#  in arr1 are the same as in arr2.
#  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


# Constraints:

# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_table = dict()
        for i, v in enumerate(arr2):
            hash_table[v] = i

        for v in arr1:
            if hash_table.get(v) == None:
                hash_table[v] = float("inf")

        arr1 = sorted(arr1, key=lambda x: hash_table[x])
        for i, v in enumerate(arr1):
            if hash_table[v] == float("inf"):
                arr1[i:] = sorted(arr1[i:])
        return arr1


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.relativeSortArray)
    t.equal(
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
        [2, 1, 4, 3, 9, 6],
    )

