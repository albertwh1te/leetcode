# 6. ZigZag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern
# on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        P     I    N
        A   L S  I G
        Y A   H R
        P     I

        The result is the combination of two part:
        P     I    N
        A     S    G
        Y     H  
        P     I
        and
                   
            L    I 
          A     R
        
        The first part index is 2n-2
        The second part index is j+(2n-2)-2i without first and last line
        """
        if numRows <= 1:
            return s
        result = ""
        size = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), size):
                result += s[j]
                if i != numRows - 1 and i != 0:
                    index = j + size - 2 * i
                    if index < len(s):
                        result += s[index]
        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.convert)
    t.equal("PAHNAPLSIIGYIR", "PAYPALISHIRING", 3)
