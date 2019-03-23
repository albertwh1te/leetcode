class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append("$")
        for c in s:
            if c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
            else:
                stack.append(c)
        return len(stack) == 1
