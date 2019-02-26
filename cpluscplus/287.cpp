// 287. Find the Duplicate Number
// Favorite

// Share
// Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
//  prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

// Example 1:

// Input: [1,3,4,2,2]
// Output: 2
// Example 2:

// Input: [3,1,3,4,2]
// Output: 3
// Note:

// You must not modify the array (assume the array is read only).
// You must use only constant, O(1) extra space.
// Your runtime complexity should be less than O(n2).
// There is only one duplicate number in the array, but it could be repeated more than once.

// Solution:
// 实际上，我们可以根据抽屉原理简化刚才的暴力法。我们不一定要依次选择数，
// 然后看是否有这个数的重复数，我们可以用二分法先选取n/2，
// 按照抽屉原理，整个数组中如果小于等于n/2的数的数量大于n/2，
// 说明1到n/2这个区间是肯定有重复数字的。
// 比如6个抽屉，如果有7个袜子要放到抽屉里，那肯定有一个抽屉至少两个袜子。
// 这里抽屉就是1到n/2的每一个数，而袜子就是整个数组中小于等于n/2的那些数。
// 这样我们就能知道下次选择的数的范围，如果1到n/2区间内肯定有重复数字
// ，则下次在1到n/2范围内找，否则在n/2到n范围内找。下次找的时候，还是找一半。

#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int countLess(int target, vector<int> nums)
{
    int sum = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (target >= nums[i])
        {
            sum++;
        }
    }
    return sum;
}

class Solution
{
  public:
    int findDuplicate(vector<int> &nums)
    {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;
        while (left <= right)
        {
            int mid = left + ((right - left) >> 1);
            if (countLess(mid, nums) > mid)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
};

int main()
{
    vector<int> test = {1, 2, 2, 3, 4};
    Solution s = Solution();
    cout << s.findDuplicate(test) << endl;
    return 1;
}