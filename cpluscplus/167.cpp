// 167. Two Sum II - Input array is sorted
// Given an array of integers that is already sorted in ascending order,
//  find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target,
//  where index1 must be less than index2.

// Note:

// Your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution and you may not use the same element twice.
// Example:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution
{
  public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int i = 0;
        int j = numbers.size() - 1;
        int sum;
        while (i < j)
        {
            sum = numbers[i] + numbers[j];
            if (sum == target)
            {
                return vector<int>{i + 1, j + 1};
            }
            else if (sum > target)
            {
                j--;
            }
            else
            {
                i++;
            }
        }
        return vector<int>{-1, -1};
    }
};

int main()
{
    Solution s = Solution();
    vector<int> test = {2, 7, 11, 15};
    int target = 9;
    // TODO:FIX THIS!
    vector<int> answer = s.twoSum(test, target);
    cout << answer[0] << answer[1] << endl;
    return 0;
}