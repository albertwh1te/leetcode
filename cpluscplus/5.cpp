// 5. Longest Palindromic Substring
#include <iostream>
#include <string>
using namespace std;

class Solution
{
  public:
    string longestPalindrome(string s)
    // We define dp(i,j)
    // dp(i,j) as following:
    // dp[i,j] = 1  if i ==j
    // =  s[i] == s[j]   if j = i+1
    // =  s[i] == s[j] && dp[i+1][j-1]  if j>i+1
    // dp(0,0) = True

    {
        int n = s.size();
        if (n <= 1)
        {
            return s;
        }

        int start;
        int max_length = 0;
        // TODO: fix error: variable-sized object may not be initialized
        bool dp[n][n] = {{false}};
        {
            for (size_t i = 0; i < s.size(); i++)
            {
                dp[i][i] = true;
                for (size_t j = 0; j < i; j++)
                {
                    dp[j][i] = (s[i] == s[j]) and ((i - j == 1) or (dp[j + 1][i - 1]));
                    if (dp[j][i] and max_length < (i - j + 1))
                    {
                        max_length = i - j + 1;
                        start = j;
                    }
                }
            }
            return s;
        }
        return s.substr(start, max_length);
    }
};

int main()
{
    Solution s = Solution();
    string t = "babad";
    cout << t << "should be 'bab' : " << s.longestPalindrome(t) << endl;
    t = "cbbd";
    cout << t << "should be 'bb' : " << s.longestPalindrome(t) << endl;
    return 0;
}