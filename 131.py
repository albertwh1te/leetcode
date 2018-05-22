class Solution(object):
    def palindrome(self, s):
        return s == s[::-1]

    def partition(self, s):
        if len(s) == 0:
            return [[]]
        results = []
        for l in range(1, len(s) + 1):
            current = s[:l]
            if self.palindrome(current) and current + s[l:] == s:
                for r in self.partition(s[l:]):
                    results.append([current] + r)
        return results


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.partition)
    r1 = [
        ["a", "a", "b"],
        ["aa", "b"],
    ]
    t.equal(r1, "aab")
