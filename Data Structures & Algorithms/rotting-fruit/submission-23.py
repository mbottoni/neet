class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        # Collect the position of all rotten and number of fresh
        rotten = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])
        # With the collect position and fresh run the simulation
        time = 0
        positions = [[-1,0],[0,-1],[0,1],[1,0]]
        while fresh > 0 and rotten:
            for _ in range(len(rotten)):
                pos = rotten.popleft()
                for dx, dy in positions:
                    ni, nj = pos[0]+dx, pos[1]+dy
                    if ni>=0 and ni<rows and nj>=0 and nj<cols:
                        if grid[ni][nj] == 1:
                            grid[ni][nj]=2
                            rotten.append([ni,nj])
                            fresh -= 1
            time += 1
        
        if fresh>0:
            return -1
        return time



