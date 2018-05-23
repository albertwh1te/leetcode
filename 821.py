class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        results = []
        index = [i for i, v in enumerate(S) if v == C]
        for x in range(len(S)):
            minium = len(S)
            for y in index:
                if abs(y - x) <= minium:
                    minium = abs(y - x)
            results.append(minium)
        return results


if __name__ == '__main__':
    print(Solution().shortestToChar("loveleetcode", "e"))
