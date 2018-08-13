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


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.combinationSum)
    r1 = [
        [2, 2, 3],
        [7]
    ]
    t.equal(r1, [2, 3, 6, 7], 7)
    r2 = [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
    t.equal(r2, [2, 3, 5], 8)
