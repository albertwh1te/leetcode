from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words)
        if length < 1 or len(s) < 1:
            return []

        size = len(words[0])

        origin_hashtable = {}
        for word in words:
            if not origin_hashtable.get(word):
                origin_hashtable[word] = 1
            else:
                origin_hashtable[word] += 1

        result = []
        for i in range(len(s) - length + 1):
            count_hashtable = {}
            j = i
            while j <= i + length * size:
                sub_string = s[j:j + size]
                if not origin_hashtable.get(sub_string):
                    break
                if not count_hashtable.get(sub_string):
                    count_hashtable[sub_string] = 1
                else:
                    count_hashtable[sub_string] += 1
                if count_hashtable[sub_string] > origin_hashtable[sub_string]:
                    break
                j += size
            if j == i + length * size:
                result.append(i)

        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.findSubstring)
    t.same_elements([0, 9], "barfoothefoobarman", ["foo", "bar"])
    t.same_elements([], "wordgoodgoodgoodbestword",
                    ["word", "good", "best", "word"])
    t.same_elements([0], "a", ["a"])
