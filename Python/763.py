# 输入: S = "ababcbacadefegdehijhklij"
# 输出: [9,7,8]
# 解释:
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Solution1: brute force
        # results = []
        # start = end = 0
        # for i in range(len(S)):
        #     end = max(end, S.rfind(S[i]))
        #     if i == end:
        #         length = end - start + 1
        #         results.append(length)
        #         start = end + 1
        # return results

        # Solution2: greedy algorithms
        results = []
        last_index = {char: index for index, char in enumerate(S)}
        start = end = 0
        for index, char in enumerate(S):
            end = max(end, last_index[char])
            if index == end:
                length = end - start + 1
                results.append(length)
                start = end + 1
        return results


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.partitionLabels)
    t.equal([9, 7, 8], "ababcbacadefegdehijhklij")
