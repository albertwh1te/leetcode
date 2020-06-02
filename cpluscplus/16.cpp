// 16. 3Sum Closest
// Given an array nums of n integers and an integer target,
//  find three integers in nums such that the sum is closest to target.
//   Return the sum of the three integers.
//   You may assume that each input would have exactly one solution.

// Example 1:

// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

// Constraints:

// 3 <= nums.length <= 10^3
// -10^3 <= nums[i] <= 10^3
// -10^4 <= target <= 10^4
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        int result = 0;
        int diff = numeric_limits<int>::max();
        sort(nums.begin(), nums.end());
        for (size_t i = 0; i < nums.size() - 1; i++)
        {
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if (abs(target - sum) < diff)
                {
                    result = sum;
                    diff = abs(target - sum);
                }
                if (target > sum)
                {

                    left++;
                }
                else if (target < sum)
                {
                    right--;
                }
                // target = sum,nothing you can move,just try another value
                else
                {
                    break;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution s = Solution();
    vector<int> nums;
    int ans;
    // nums = {-1, 2, 1, -4};
    // ans = s.threeSumClosest(nums, 1);
    // cout << ans << endl; // 2
    // nums = {1, 1, 1, 0};
    // ans = s.threeSumClosest(nums, -100);
    // cout << ans << endl; // 2
    nums = {0, 2, 1, -3};
    ans = s.threeSumClosest(nums, 1);
    cout << ans << endl; // 2

    return 0;
}