#  17. Letter Combinations of a Phone Number

#  Given a string containing digits from 2-9 inclusive,
#  return all possible letter combinations that the number could represent.

#  A mapping of digit to letters (just like on the telephone buttons) is given below.
#  Note that 1 does not map to any letters.
from typing import List


class Solution:
    key_map = {
        "2": "abc",
        "3": "edf",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(Solution.key_map[digits[0]])
        results = []
        for result in self.letterCombinations(digits[1:]):
            for letter in Solution.key_map[digits[0]]:
                results.append(letter + result)
        return results


if __name__ == "__main__":
    from util import Test

    t = Test(Solution().letterCombinations)

    t.same_elements(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "23")
