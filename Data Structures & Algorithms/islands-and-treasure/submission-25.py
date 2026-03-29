class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visi = set()
        q = deque()

        def visit(i, j):
            if i>=0 and j>=0 and i<m and j<n:
                if grid[i][j]==2147483647:
                    grid[i][j] = dist
                    q.append([i,j])
            



        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visi.add((i, j))

        dist = 0 
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                grid[cur[0]][cur[1]] = dist
                visit(cur[0]+1, cur[1])
                visit(cur[0]-1, cur[1])
                visit(cur[0], cur[1]+1)
                visit(cur[0], cur[1]-1)
            dist += 1

