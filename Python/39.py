# 39. Combination Sum

# Given a set of candidate numbers (candidates) (without duplicates) and
#  a target number (target), find all unique combinations in candidates
#  where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target < 0:
            return []
        if target == 0:
            return [[]]

        results = []
        for candidate in candidates:
            for result in self.combinationSum(candidates, target - candidate):
                tmp = sorted(result + [candidate])
                if tmp not in results:
                    results.append(tmp)
        return results


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.combinationSum)
    r1 = [[2, 2, 3], [7]]
    t.equal(r1, [2, 3, 6, 7], 7)
    r2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    t.equal(r2, [2, 3, 5], 8)
