class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1].isdigit():
            return int(str(x)[::-1]) == x
        return False
