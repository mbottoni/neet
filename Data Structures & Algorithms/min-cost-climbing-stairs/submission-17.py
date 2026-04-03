class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ar = [None] * n
        def dfs(i):
            if i > n - 1:
                return 0
            if ar[i] != None:
                return ar[i]
            ar[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return ar[i]

        return min(dfs(0), dfs(1))






        