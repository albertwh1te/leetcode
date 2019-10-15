// 387. First Unique Character in a String
// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.
#include <string>
using namespace std;
class Solution
{
public:
    int firstUniqChar(string s)
    {
        int times[52] = {0};
        int index;
        for (char &c : s)
        {
            index = int(c) - int('a');
            times[index] += 1;
        }
        for (int i = 0; i < s.size(); i++)
        {
            index = int(s[i]) - int('a');
            if (times[index] == 1)
            {
                return i;
            }
        }

        return -1;
    }
};