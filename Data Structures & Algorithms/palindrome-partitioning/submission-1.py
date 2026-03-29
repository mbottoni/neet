class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_pal(s):
            return s[::-1] == s

        def backtrack(start, current):
            if start == len(s):
                result.append(list(current))
                return
            for end in range(start + 1, len(s) + 1):
                if is_pal(s[start:end]):
                    current.append(s[start:end])
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result