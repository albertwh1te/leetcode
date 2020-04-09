#  Counting Elements

# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there're duplicates in arr, count them seperately.


# Example 1:

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
# Example 3:

# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
# Example 4:

# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        hash_table = dict()
        for number in arr:
            if hash_table.get(number) == None:
                hash_table[number] = 0
            else:
                hash_table[number] += 1
        for number in arr:
            if hash_table.get(number+1) != None:
                hash_table[number+1] -= 1
                result +=1 
        return result



if __name__ == "__main__":
    from util import Test

    t = Test(Solution().countElements)
    t.equal(2, [1, 1, 2, 2])
    t.equal(3, [1, 3, 2, 3, 5, 0])
    t.equal(0, [1, 1, 3, 3, 5, 5, 7, 7])
    t.equal(2, [1, 2, 3])
