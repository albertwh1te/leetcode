# 84. Largest Rectangle in Histogram

# Given n non-negative integers representing the histogram's bar height
#  where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

# Solution:

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        max_area = float("-inf")
        # from bottom to top ,value of index is from low to high
        min_stack = []
        for i, v in enumerate(heights):
            while len(min_stack) and v < heights[min_stack[-1]]:
                current_index = min_stack.pop()
                left = -1 if len(min_stack) == 0 else min_stack[-1]
                # right is i, because current index is pop out when meet heights[i]
                current_area = (i - left - 1) * heights[current_index]
                max_area = max(current_area, max_area)

            # case 1: is a empty stack push in
            # case 2: no more value less than heights[i]
            min_stack.append(i)

        right = len(heights)
        while len(min_stack):
            current_index = min_stack.pop()
            left = -1 if len(min_stack) == 0 else min_stack[-1]
            current_area = (right - left - 1) * heights[current_index]
            max_area = max(current_area, max_area)

        return max_area


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.largestRectangleArea)
    t.equal(10, [2, 1, 5, 6, 2, 3])
