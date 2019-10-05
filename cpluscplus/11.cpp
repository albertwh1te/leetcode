// 11. Container With Most Water

// Given n non - negative integers a1, a2, ..., an,
// where each represents a point at coordinate(i, ai).
// n vertical lines are drawn
// such that the two endpoints of line i is at(i, ai)
//  and (i, 0).
// Find two lines,
// which together with x - axis forms a container,
// such that the container contains the most water.

#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0;
        int right = height.size() - 1;
        int h = 0;
        // area = h * (right-left)
        int area = 0;
        int maxArea = 0;
        while (left < right)
        {
            h = min(height[left], height[right]);
            area = h * (right - left);
            maxArea = max(maxArea, area);
            if (height[left] > height[right])
            {
                right--;
            }
            else
            {
                left++;
            }
        }
        return maxArea;
    }
};