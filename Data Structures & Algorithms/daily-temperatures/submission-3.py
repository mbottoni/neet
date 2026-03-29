class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # (temp,index)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                answer[stackI] = abs(stackI - i)
            stack.append((temp, i))

        return answer
        