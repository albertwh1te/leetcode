
# 1072. Flip Columns For Maximum Number of Equal Rows


# Given a matrix consisting of 0s and 1s,
# we may choose any number of columns in the matrix and flip every cell in that column.
# Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

# Return the maximum number of rows that have all values equal after some number of flips.

 

# Example 1:

# Input: [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:

# Input: [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:

# Input: [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.
from typing import List
from collections import defaultdict

class Solution:
    """
    we don't need to truly flipped the columns,there is two case we can get the right result
        case 1: They are the same before the flipping, e.g. [[0,0,1,0,0],[0,0,1,0,0]].
        case 2: They are one's complement for each other before the flipping e.g. [0,0,1,0,0],[1,1,0,1,1]]. 

    so the key point is understand what we need memory is the pattern  [0,0,1] and [1,1,0] is the same pattern
    we can record all of pattern into a hash table and return the max one
    time complexity O(m*n)
    space complexity 0(m*n),  hash table key size m , every key has n length
    """
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        result = 0
        hash_table = defaultdict(int)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            pattern = [] 
            for j in range(n):
                # they are the same pattern choose any one you want , [0,0,1] and [1,1,0] is the same pattern
                # pattern.append(matrix[i][-1] ^ matrix[i][j])
                pattern.append(matrix[i][0] ^ matrix[i][j])
            hash_table[tuple(pattern)] += 1
            result = max(result,hash_table[tuple(pattern)])
        return result
                

if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.maxEqualRowsAfterFlips)
    t.equal(1,[[0,1],[1,1]])
    t.equal(2,[[0,1],[1,0]])
    t.equal(2,[[0,0,0],[0,0,1],[1,1,0]])
    t.equal(3,[[0,0,0],[0,0,1],[1,1,0],[0,0,1]])

    
