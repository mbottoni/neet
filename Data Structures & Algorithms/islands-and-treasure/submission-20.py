class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        #q = deque()
        q = list()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c]) # Will have simillar performance to deque

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c]) # Similar perrformance
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                #r, c = q.popleft()
                r, c = q.pop(0)
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1