# 241. Different Ways to Add Parentheses
# Given a string of numbers and operators,
#  return all possible results from computing all
#  the different possible ways to group numbers and operators.
#  The valid operators are +, - and *.

# Example 1:

# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:

# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not hasattr(self, "memo"):
            self.memo = {}
        if self.memo.get(input):
            return self.memo[input]

        result = []
        for index, value in enumerate(input):
            if value == "+" or value == "*" or value == "-":
                right = self.diffWaysToCompute(input[:index])
                left = self.diffWaysToCompute(input[index + 1 :])
                for i in range(len(right)):
                    for j in range(len(left)):
                        if value == "+":
                            result.append(right[i] + left[j])
                        elif value == "-":
                            result.append(right[i] - left[j])
                        elif value == "*":
                            result.append(right[i] * left[j])
        if len(result) == 0:
            result.append(int(input))
        self.memo[input] = result
        return result


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.diffWaysToCompute)
    t.same_elements([0, 2], "2-1-1")
    t.same_elements([-34, -14, -10, -10, 10], "2*3-4*5")
