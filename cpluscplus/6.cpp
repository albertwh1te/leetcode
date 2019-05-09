#include <iostream>
#include <string>
using namespace std;

class Solution
{
  public:
    string convert(string s, int numRows)
    {
        if (numRows <= 1)
        {
            return s;
        }
        string result;
        int size = 2 * numRows - 2;
        for (int i = 0; i < numRows; i++)
        {
            for (int j = i; j < s.size(); j += size)
            {
                result += s[j];
                if (i != 0 && i != numRows - 1)
                {
                    int index = j + size - 2 * i;
                    if (index < s.size())
                    {
                        result += s[index];
                    }
                }
            }
        }
        return result;
    }
};