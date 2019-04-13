# 85. Maximal Rectangle

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = float("-inf")
        min_stack = []
        for i, v in enumerate(heights):
            while len(min_stack) != 0 and v < heights[min_stack[-1]]:
                current_index = min_stack.pop()
                left = min_stack[-1] if len(min_stack) else -1
                current_area = (i - left - 1) * heights[current_index]
                maximum = max(current_area, maximum)
            min_stack.append(i)

        right = len(heights)
        while len(min_stack):
            current_index = min_stack.pop()
            left = min_stack[-1] if len(min_stack) else -1
            current_area = (right - left - 1) * heights[current_index]
            maximum = max(current_area, maximum)
        return maximum

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maximum = float("-inf")
        tmp = [0 for _ in matrix[0]]
        for i, _ in enumerate(matrix):
            for index, value in enumerate(matrix[i]):
                tmp[index] = tmp[index] + 1 if value == '1' else 0
            current = self.largestRectangleArea(tmp)
            maximum = max(current, maximum)
        return maximum


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.maximalRectangle)
    t.equal(6, [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
    t.equal(1, [["1"]])
