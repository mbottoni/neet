class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '{':
                stack = stack + ['{']
            elif s[i] == '(':
                stack = stack + ['(']
            elif s[i] == '[':
                stack = stack + ['[']
            elif len(stack) > 0 and s[i] == '}' and stack[-1]=='{':
                stack = stack[:-1]
            elif len(stack) > 0 and s[i] == ')' and stack[-1]=='(':
                stack = stack[:-1]
            elif len(stack) > 0 and s[i] == ']' and stack[-1]=='[':
                stack = stack[:-1]
            else:
                return False


        if len(stack)==0:
            return True
        return False
        