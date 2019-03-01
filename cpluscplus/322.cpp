#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
  int coinChange(vector<int> &coins, int amount)
  {
    vector<int> dp(amount + 1, -1);
    dp[0] = 0;
    for (int v = 0; v <= amount; v++)
    {
      vector<int> tmp;
      for (int i = 0; i < coins.size(); i++)
      {
        if ((v - coins[i] >= 0) && (dp[v - coins[i]] != -1))
        {
          if (dp[v] == -1)
          {
            dp[v] = dp[v - coins[i]] + 1;
          }
          else
          {
            dp[v] = min(dp[v], dp[v - coins[i]] + 1);
            cout << dp[v] << endl;
          }
        }
      }
    }
    return dp[amount];
  }
};

int main()
{
  vector<int> test = {1, 3, 5};
  int target = 11;
  Solution s = Solution();
  int answer = s.coinChange(test, target);
  cout << answer << endl;
  return 0;
}