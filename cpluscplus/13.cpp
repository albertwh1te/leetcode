// 13. Roman to Integer

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right.
//  However, the numeral for four is not IIII.
//  Instead, the number four is written as IV.
//  Because the one is before the five we subtract it making four.
//  The same principle applies to the number nine,
//  which is written as IX. There are six instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9.
// X can be placed before L (50) and C (100) to make 40 and 90.
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given a roman numeral, convert it to an integer.
//  Input is guaranteed to be within the range from 1 to 3999.
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        int result = 0;
        unordered_map<char, int> hash;
        hash['I'] = 1;
        hash['V'] = 5;
        hash['X'] = 10;
        hash['L'] = 50;
        hash['C'] = 100;
        hash['D'] = 500;
        hash['M'] = 1000;
        // iter from right to left III

        for (int i = (s.size() - 1); i > -1; i--)
        {

            // Roman numerals are usually written largest to smallest
            //  from left to right. If not means special case(IV=4 or IX=9)
            if (i > 0 && hash[s[i]] > hash[s[i - 1]])
            {
                // minors two times of s[i-1] because next will add s[i-1]
                result += hash[s[i]] - hash[s[i - 1]] * 2;
            }
            else
            {
                result += hash[s[i]];
            }
        }
        return result;
    }
};

int main()
{
    Solution s = Solution();
    int ans = 0;
    ans = s.romanToInt("III");
    std::cout << ans << std::endl;
    ans = s.romanToInt("IV");
    std::cout << ans << std::endl;
    ans = s.romanToInt("IX");
    std::cout << ans << std::endl;
    ans = s.romanToInt("LVIII");
    std::cout << ans << std::endl;
    ans = s.romanToInt("MCMXCIV");
    std::cout << ans << std::endl;
    return 0;
}