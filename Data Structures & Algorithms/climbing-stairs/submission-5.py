class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        def dfs(i):
            if i == n:
                return 1  # fix 1: reached top = 1 valid way
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            count = dfs(i+1) + dfs(i+2)  # fix 2: removed the spurious + 1
            cache[i] = count
            return cache[i]
        return dfs(0)