// Determine whether an integer is a palindrome.An integer is a palindrome when it reads the same backward as forward.

//     Example 1 :

//     Input : 121 Output : true Example 2 :

//     Input : -121 Output : false
//      Explanation : From left to right,
//     it reads - 121. From right to left, it becomes 121 -.Therefore it is not a palindrome.

//       Example 3 :

//     Input : 10 Output : false Explanation : Reads 01 from right to left.Therefore it is not a palindrome.Follow up :

//     Coud you solve it without converting the integer to a string
//     ?
#include <iostream>
using namespace std;
class Solution
{
public:
    bool isPalindrome(int x)
    {
        // revert last half of number (1221 means 12 == 12)
        //  Now let's think about how to revert the last half of the number.
        //  For number 1221, if we do 1221 % 10,
        //  we get the last digit 1,
        //  to get the second to the last digit,
        //  we need to remove the last digit from 1221,
        //  we could do so by dividing it by 10,
        //  1221 / 10 = 122.
        //  Then we can get the last digit again by doing a modulus by 10,
        //  122 % 10 = 2,
        //  and if we multiply the last digit by 10 and add the second last digit,
        //  1 * 10 + 2 = 12, it gives us the reverted number we want.
        //  Continuing this process would give us the reverted number with
        //  more digits.
        if (x < 0 || (x % 10 == 0 && x != 0))
        {
            return false;
        }
        int lastHalf = 0;
        while (x > lastHalf)
        {
            lastHalf = lastHalf * 10 + x % 10;
            x = x / 10;
        }
        // case 1 :  1221 for 12 == 12
        // case 2 :  121  for 12/10 == 12
        return lastHalf == x || lastHalf / 10 == x;
    }
};

int main()
{
    Solution s = Solution();
    int ans = 0;
    ans = s.isPalindrome(123);
    cout << ans << endl;
    ans = s.isPalindrome(121);
    cout << ans << endl;
    ans = s.isPalindrome(1221);
    cout << ans << endl;
    ans = s.isPalindrome(-121);
    cout << ans << endl;
    return 0;
}