class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == '+':
                el2 = stack.pop()
                el1 = stack.pop()
                stack.append(el1+el2)
            elif tok == '-':
                el2 = stack.pop()
                el1 = stack.pop()
                stack.append(el1-el2)
            elif tok == '*':
                el2 = stack.pop()
                el1 = stack.pop()
                stack.append(el1*el2)
            elif tok == '/':
                el2 = stack.pop()
                el1 = stack.pop()
                stack.append(int(el1 / el2))
            else:
                stack.append(int(tok))

        return stack[-1]
        