// 17. Letter Combinations of a Phone Number
// Given a string containing digits from 2-9 inclusive,
//  return all possible letter combinations that the number could represent.

// A mapping of digit to letters (just like on the telephone buttons) is
//  given below. Note that 1 does not map to any letters.

// Example:

// Input: "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution
{
private:
    vector<string> number2string = ["abc", ] vector<string> help(vector<string> ans, string digits, int index) {
        vector<string> ans = {};
        if (index == (digits.size() - 1))
        {
        }
    }

    public : vector<string>
             letterCombinations(string digits)
    {
        vector<string> ans = {};
        return help(ans, digits, 0);
    }
};
int main()
{
    Solution s = Solution();
    string d;
    vector<string> ans;
    d = "23";
    ans = s.letterCombinations(d);
    cout << ans << endl;
}
