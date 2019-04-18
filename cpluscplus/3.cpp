#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
  int lengthOfLongestSubstring(string s)
  {
    int code_arr[255] = {0};
    int length = s.length();
    int left = 0;
    int right = 0;
    int result = 0;
    while (right < length)
    {
      if (code_arr[(int)s[right]] > 0)
      {
        left = max(code_arr[(int)s[right]], left);
      }
      code_arr[(int)s[right]] = right + 1;
      right++;
      result = max(right - left, result);
    }
    return result;
  }
};

int main()
{
  string t = "abc";
  Solution s = Solution();
  cout << t << ":" << s.lengthOfLongestSubstring(t) << endl;
  t = "bbbb";
  cout << t << ":" << s.lengthOfLongestSubstring(t) << endl;
  t = "pwwkew";
  cout << t << ":" << s.lengthOfLongestSubstring(t) << endl;
  return 0;
}