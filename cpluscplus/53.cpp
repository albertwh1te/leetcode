#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        for (int i = 1; i < dp.size(); i++) {
            dp[i] = max(dp[i - 1] + nums[i], nums[i]);
        };
        return *max_element(dp.begin(), dp.end());
    }
};

int main() {
    vector<int> num;
    int result;
    num = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    result = Solution().maxSubArray(num);
//    6
    cout << result << endl;

    num = {1};
    result = Solution().maxSubArray(num);

//    1
    cout << result << endl;

    num = {5, 4, -1, 7, 8};
    result = Solution().maxSubArray(num);

//    23
    cout << result << endl;
}


