class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visit_island(i, j):
            m, n = len(grid), len(grid[0])
            if i >= 0  and j >=0 and i < m and j < n:
                if grid[i][j]==1:
                    grid[i][j] = 0
                    return 1 + visit_island(i+1, j) + visit_island(i-1, j) + visit_island(i, j+1) + visit_island(i, j-1)
                else:
                    return 0
            else:
                return 0








        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area = visit_island(i, j)
                    maxArea = max(maxArea, area)
        return maxArea
        