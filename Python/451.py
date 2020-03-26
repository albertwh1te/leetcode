# 451. Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


class Solution:
    def frequencySort(self, s: str) -> str:
        frequencey = dict()
        for i in s:
            if frequencey.get(i) == None:
                frequencey[i] = 1
            else:
                frequencey[i] += 1
        frequencey = sorted(frequencey.items(), key=lambda x: -x[-1])
        return "".join((char * times for char, times in frequencey))


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.frequencySort)
    t.equal("eetr", "tree")
    t.equal("cccaaa", "cccaaa")
    t.equal("bbAa", "Aabb")
