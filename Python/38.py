# 38. Count and Say

# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"


class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"
        # add one symbol for corner case
        before = self.countAndSay(n - 1) + "$"
        result = ""
        count = 1
        for i in range(len(before) - 1):
            if before[i] == before[i + 1]:
                count += 1
            else:
                # corner case is before[i+1] == "$" so will go here
                result = result + str(count) + before[i]
                count = 1
        return result


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().countAndSay)
    t.equal("1", 1)
    t.equal("1211", 4)
    t.equal("111221", 5)
    t.equal("13211311123113112211", 10)
