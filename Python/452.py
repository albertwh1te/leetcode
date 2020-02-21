# 452. Minimum Number of Arrows to Burst Balloons

# There are a number of spherical balloons spread in two-dimensional space.
#  For each balloon,
#  provided input is the start and end coordinates of the horizontal diameter.
#  Since it's horizontal,
#  y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice.
#  Start is always smaller than end. There will be at most 104 balloons.

# An arrow can be shot up exactly vertically from different points along the x-axis.
#  A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
#  There is no limit to the number of arrows that can be shot.
#  An arrow once shot keeps travelling up infinitely.
#  The problem is to find the minimum number of arrows that must be shot to burst all balloons.

# Example:

# Input:
# [[10,16], [2,8], [1,6], [7,12]]

# Output:
# 2

# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
from typing import List


class Solution:
    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        length = len(points)
        if length < 1:
            return 0

        result = 1
        points.sort(key=lambda x: (x[0], x[1]))
        start = points[0][0]
        end = points[0][1]
        for i in range(1, length):
            start = max(start, points[i][0])
            end = min(end, points[i][1])
            if start > end:
                result += 1
                start = points[i][0]
                end = points[i][1]
        return result

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 1:
            return 0
        result = 0
        current_end = float("-inf")
        points.sort(key=lambda x: x[1])
        for start, end in points:
            if start > current_end:
                result += 1
                current_end = end
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.findMinArrowShots)
    t.equal(2, [[10, 16], [2, 8], [1, 6], [7, 12]])
    t.equal(2, [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
