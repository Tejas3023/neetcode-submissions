class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                ch = stack[-1]
                stack.pop()
                if not (s[i]==')' and ch == '('or s[i]=='}' and ch == '{'or s[i]==']' and ch == '['):
                    return False
        return len(stack) == 0