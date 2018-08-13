class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        result = []
        direction = {
            "U": "D",
            "D": "U",
            "L": "R",
            "R": "L"
        }
        for move in moves:
            if direction[move] in result:
                result.remove(direction[move])
            else:
                result.append(move)
        return result == []


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.judgeCircle)
    t.equal(True, "UD")
    t.equal(False, "LL")
