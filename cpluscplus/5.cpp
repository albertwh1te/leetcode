// 5. Longest Palindromic Substring
#include <iostream>
#include <vector>
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
        vector<bool> row(n, false);
        vector<vector<bool>> dp(n, row);
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
        }
        //  corner case
        if (max_length == 0)
        {
            return s.substr(start, 1);
        }
        return s.substr(start, max_length);
    }
};

int main()
{
    Solution s = Solution();
    string t = "babad";
    string r = s.longestPalindrome(t);
    cout << t << "should be 'bab' : " << r << "\n"
         << endl;
    t = "cbbd";
    r = s.longestPalindrome(t);
    cout << t << "should be 'bb' : " << r << "\n"
         << endl;
    t = "ac";
    r = s.longestPalindrome(t);
    cout << t << "should be 'a' : " << r << "\n"
         << endl;
    return 0;
}