#  Backspace String Compare

# Given two strings S and T,
# return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # i for s
        i = len(S) - 1
        back_i = 0
        # j for T
        j = len(T) - 1
        back_j = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    back_i += 1
                    i -= 1
                elif back_i > 0:
                    back_i -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":

                    back_j += 1
                    j -= 1
                elif back_j > 0:
                    back_j -= 1
                    j -= 1
                else:
                    break

            if (i >= 0) != (j >= 0):
                return False

            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            i -= 1
            j -= 1

        return True


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.backspaceCompare)
    S = "ab#c"
    T = "ad#c"
    t.equal(True, S, T)
    S = "ab##"
    T = "c#d#"
    t.equal(True, S, T)
    S = "a#c"
    T = "b"
    t.equal(False, S, T)
    S = "bbbextm"
    T = "bbb#extm"
    t.equal(False, S, T)
