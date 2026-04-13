class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    rotten.append((i, j))

        minutes = 0
        q = deque(rotten)
        while q:
            for _ in range(len(q)):  # process level by level
                pos_i, pos_j = q.popleft()
                for moves in [(-1,0), (1,0), (0,1), (0,-1)]:
                    ni, nj = pos_i+moves[0], pos_j+moves[1]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:  # bounds check
                        q.append((ni,nj))
                        grid[ni][nj] = 2

            minutes += 1

        # Check if any fresh orange remains
        if any(grid[i][j] == 1 for i in range(m) for j in range(n)):
            return -1

        return max(0,minutes-1)