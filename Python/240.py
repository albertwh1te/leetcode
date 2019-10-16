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
# ]
# Given target = 5, return true.


# Given target = 20, return false.
class Solution:
    def binary_search(self, array, target, left, right):
        while left < right:
            mid = left + ((right - left) >> 1)
            if array[mid] == target:
                return True
            elif array[mid] < target:
                return self.binary_search(array, target, mid, right)
            elif array[mid] > target:
                return self.binary_search(array, target, left, mid)
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        pass


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.searchMatrix)
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    t.equal(True, 5)
    t.equal(False, 20)
