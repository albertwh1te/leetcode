#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        vector<int> dp(cost.size() + 1, 0);
        for (size_t i = 2; i < cost.size() + 1; i++)
        // You can start at first stair or second stair,
        //  so dp[0] and dp[1] is 0.
        {
            dp[i] = min(
                cost[i - 2] + dp[i - 2], cost[i - 1] + dp[i - 1]);
        }
        return dp[cost.size()];
    }
};

int main()
{
    Solution s = Solution();

    vector<int> cost1 = {10, 15, 20};
    int answer1 = s.minCostClimbingStairs(cost1);
    cout << answer1 << endl;

    vector<int> cost2 = {0, 0, 1, 1};
    int answer2 = s.minCostClimbingStairs(cost2);
    cout << answer2 << endl;

    return 0;
}