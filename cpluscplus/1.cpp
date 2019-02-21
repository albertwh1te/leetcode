// 1. Two Sum
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution
{
  public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<pair<int, int>> pairs;
        pair<int, int> tmp;
        for (int i = 0; i < nums.size(); i++)
        {
            tmp.first = nums[i];
            tmp.second = i;
            pairs.push_back(tmp);
        }
        sort(pairs.begin(), pairs.end());
        int i = 0;
        int j = pairs.size() - 1;
        while (i < j)
        {
            if (pairs[i].first + pairs[j].first == target)
            {
                return vector<int>{pairs[i].second, pairs[j].second};
            }
            else if (pairs[i].first + pairs[j].first < target)
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return vector<int>{-1, -1};
    };
    vector<int> twoSum2(vector<int> &nums, int target)
    {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++)
        {
            m[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            if (m.count(diff) && m[diff] != i)
            {
                return vector<int>{i, m[diff]};
            }
        }
        return vector<int>{-1, -1};
    };
};

int main()
{
    vector<int> test = {2, 7, 11, 15};
    int target = 9;
    Solution s = Solution();
    vector<int> answer = s.twoSum(test, target);
    vector<int> answer2 = s.twoSum2(test, target);
    cout << answer[0] << answer[1] << endl;
    cout << answer2[0] << answer2[1] << endl;
    return 0;
}