class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit_land(i, j):
            if i<len(grid) and j<len(grid[0]) and i>=0 and j>=0 and grid[i][j]=='1':
                grid[i][j] = 'x'
                visit_land(i+1, j)
                visit_land(i-1, j)
                visit_land(i, j-1)
                visit_land(i, j+1)
        
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    visit_land(i,j)

        return count
        