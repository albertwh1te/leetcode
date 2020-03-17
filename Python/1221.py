# 1221. Split a String in Balanced Strings

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.


# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


# Constraints:

# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        balance = 0
        for i, v in enumerate(s):
            if v == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0 and i != 0:
                result += 1
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.balancedStringSplit)
    t.equal(3, "RLLLLRRRLR")

