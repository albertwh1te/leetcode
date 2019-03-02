// 64. Minimum Path Sum

// Given a m x n grid filled with non-negative numbers,
//  find a path from top left to bottom right
//  which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Example:

// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int minPathSum(vector<vector<int>> &grid)
    {
        int dp[grid.size()][grid[0].size()];
        dp[grid.size() - 1][grid[0].size() - 1] = grid[grid.size() - 1][grid[0].size() - 1];
        for (int j = grid[0].size() - 2; j >= 0; j++)
        {
            dp[grid.size() - 1][j] = dp[grid.size() - 1][j - 1] + grid[grid.size() - 1][j];
        }
        // for (int i = grid.size() - 2; i > -0; i++)
        // {
        //     dp[i][grid[0].size() - 1] = dp[i - 1][grid[0].size() - 1] + grid[i][grid[0].size() - 1];
        // }
        // return dp[0][0];
        return dp[grid.size() - 1][grid[0].size() - 1];
    }
};

int main()
{
    vector<vector<int>> test = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}};
    Solution s = Solution();
    int answer = s.minPathSum(test);
    cout << answer << endl;
    return 0;
}