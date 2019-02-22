# 744. Find Smallest Letter Greater Than Target

# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:


class Solution:
    def nextGreatestLetter(self, letters: 'List[str]', target: 'str') -> 'str':
        for i, v in enumerate(sorted(letters)):
            if target < v:
                return letters[i]
            if target == v:
                if letters[(i + 1) % len(letters)] != v:
                    return letters[(i + 1) % len(letters)]
        return letters[0]