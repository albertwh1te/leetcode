#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;
        // if reach the last columns,keep go down
        for (size_t i = 0; i < m; i++)
        {
            dp[i][0] = 1;
        }
        // if reach the last rows,keep go right
        for (size_t i = 0; i < n; i++)
        {
            dp[0][i] = 1;
        }
        // state transition equation dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        for (size_t i = 1; i < m; i++)
        {
            for (size_t j = 1; j < n; j++)
            {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                cout << dp[i][j] << "i: " << i << "j: " << j << endl;
            }
        }
        return dp[m - 1][n - 1];
    }
};

int main()
{
    int m, n, answer;
    Solution s = Solution();
    m = 3;
    n = 2;
    answer = s.uniquePaths(m, n);
    cout << answer << endl;
}