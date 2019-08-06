# 8. String to Integer (atoi)

# implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first
#  non-whitespace character is found.
#  Then, starting from this character,
#  takes an optional initial plus or minus sign followed by as many numerical digits as possible,
#  and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number,
#  which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number,
#  or if no such sequence exists because either str is empty or it contains only whitespace
#  characters, no conversion is performed.

# If no valid conversion could be performed,
# a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42
# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.


class Solution:
    def myAtoi(self, str: str) -> int:
        # init constatnt for 32-bit signed integer
        INT_MIN = 2**(32 - 1)
        start = 0
        end = 0
        for i, v in enumerate(str):
            if not start and not v.isdigit(
            ) and v != " " and v != "-" and v != "+":
                return 0
            if v.isdigit():
                start = i
                break
        if start >= 1:
            for v in (str[:start - 1]):
                if v != " ":
                    return 0

        flag = False
        for i, v in enumerate(str):
            if v.isdigit() and i >= start:
                end = i + 1
                flag = True
            if not v.isdigit() and flag:
                break

        # no value
        if not (end - start):
            return 0

        value = int(str[start:end])

        flag = ""
        if start > 0:
            flag = str[start - 1]

        if flag == "-":
            value *= -1

        # check if beyond limit
        if abs(value) >= INT_MIN:
            return INT_MIN - 1 if value > 0 else (-1 * INT_MIN)
        else:
            return value


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.myAtoi)
    t.equal(42, "42")
    t.equal(-42, "   -42")
    t.equal(-2147483648, "-91283472332")
    t.equal(3, "3.1415")
    t.equal(0, "-+1")
    t.equal(0, "words with 2000")
    t.equal(0, "+-2")