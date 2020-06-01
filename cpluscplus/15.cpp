// 15. 3Sum
//
// Given an array nums of n integers,
//  are there elements a, b, c in nums
//  such that a + b + c = 0 ?
//  Find all unique triplets in the array
//  which gives the sum of zero.

// Given array nums = [ -1, 0, 1, 2, -1, -4 ],
//             A solution set is : [
//                 [ -1, 0, 1 ],
//                 [ -1, -1, 2 ]
//             ]
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    // for 0 to length-2
    // if same as former: contine
    // use two pointer left and right
    // find sum = equals zero add result to results
    // contine to find (remember skip the same value for both side!)
    //  if less than zero increase the left
    //  if great than zero decrease the right
    {
        vector<vector<int>> results = {};
        if (nums.size() < 2)
        {
            return results;
        }
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
            {
                continue;
            }
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0)
                {
                    results.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1])
                    {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1])
                    {
                        right--;
                    }
                }
                else if (sum < 0)
                {
                    left++;
                }
                else
                // sum greate than zero, decrease right
                {
                    right--;
                }
            }
        }
        return results;
    }
};

void show_2d_array(vector<vector<int>> ans)
{
    std::cout << "[ ";
    for (vector<int> l : ans)
    {
        std::cout << "[ ";
        for (int n : l)
        {
            std::cout << n << ", ";
        }
        std::cout << " ],";
    }
    std::cout << " ]" << std::endl;
}

int main()
{
    Solution s = Solution();
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> ans = s.threeSum(nums);
    show_2d_array(ans);
    nums = {};
    ans = s.threeSum(nums);
    show_2d_array(ans);
    nums = {0};
    ans = s.threeSum(nums);
    show_2d_array(ans);
    nums = {-1, 0, 1, 2, -1, -4};
    ans = s.threeSum(nums);
    show_2d_array(ans);

    return 0;
}