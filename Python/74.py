# 74. Search a 2D Matrix
# Write an efficient algorithm that searches
#  for a value in an m x n matrix.
#  This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
from util import equal
from typing import List


def search_line(line: List[int], target: int) -> bool:
    left = 0
    right = len(line) - 1
    while (left <= right):
        mid = left + ((right - left) >> 1)
        if line[mid] == target:
            return True
        elif line[mid] > target:
            right = mid - 1
        elif line[mid] < target:
            left = mid + 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1:
            return False
        if len(matrix) == 1:
            return search_line(matrix[0], target)
        left = 0
        right = len(matrix) - 1
        flag = 0
        while (left <= right):
            mid = left + ((right - left) >> 1)
            if matrix[mid][0] == target:
                return True
            # smaller before and bigger now, check current line
            elif matrix[mid][0] > target and flag == -1:
                return search_line(matrix[mid], target)
            # bigger before and smaller now, check the line before
            elif matrix[mid][0] < target and flag == 1:
                return search_line(matrix[mid - 1], target)

            # bigger before and bigger now ,keep moving
            elif matrix[mid][0] > target:
                right = mid - 1
            # smaller before and  smaller now ,keep moving
            elif matrix[mid][0] < target:
                left = mid + 1
        return search_line(matrix[mid - 1], target) or search_line(
            matrix[mid], target)


def main():
    matrix = [[1, 3, 5, 7]]
    equal(Solution().searchMatrix(matrix, 3), True)
    matrix = [[22, 2, 2, 2, 2, 2]]
    equal(Solution().searchMatrix(matrix, 3), False)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    equal(Solution().searchMatrix(matrix, 16), True)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    equal(Solution().searchMatrix(matrix, 3), True)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    equal(Solution().searchMatrix(matrix, 13), False)


if __name__ == '__main__':
    main()
