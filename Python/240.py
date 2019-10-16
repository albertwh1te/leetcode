# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]https://www.jianshu.com/p/b088c92930a0
# Given target = 5, return true.
# Given target = 20, return false.

# Solution:
# Search from last item in first row,if bigger than target go left,
# if less than target go down, if reach the head or reach the bottom,
# return false.


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        # less than the smallest value or bigger than biggest value
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        y = 0
        x = len(matrix[0]) - 1
        while y <= (len(matrix) - 1) and x >= 0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            elif matrix[y][x] > target:
                x -= 1
        return False


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.searchMatrix)
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    t.equal(True, matrix, 5)
    t.equal(False, matrix, 20)
    matrix = [[-5]]
    t.equal(True, matrix, -5)
