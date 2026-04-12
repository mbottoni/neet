from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        def run(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i < 0 or i >= m or j >= n or j < 0:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            else:
                count = run(i+1,j) + run(i,j+1)
                dp[(i,j)]=count
                return count

        return run(0, 0)
        