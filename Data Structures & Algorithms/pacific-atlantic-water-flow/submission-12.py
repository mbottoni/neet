class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def can_pacific(i, j, h):
            if i>=0 and j>=0 and i<ROWS and j<COLS and (i,j) not in visit:
                visit.add((i,j))
                if heights[i][j] > h:
                    visit.remove((i,j))
                    return False
                else:
                    return True and (can_pacific(i-1, j, heights[i][j]) or can_pacific(i, j+1, heights[i][j]) or can_pacific(i+1, j, heights[i][j]) or can_pacific(i, j-1, heights[i][j]))
            elif i < 0 or j < 0:
                return True
            else:
                return False

        def can_atlantic(i, j, h):
            if i>=0 and j>=0 and i<ROWS and j<COLS and (i,j) not in visit:
                visit.add((i,j))
                if heights[i][j] > h:
                    visit.remove((i,j))
                    return False
                else:
                    return True and (can_atlantic(i-1, j, heights[i][j]) or can_atlantic(i, j+1, heights[i][j]) or can_atlantic(i+1, j, heights[i][j]) or can_atlantic(i, j-1, heights[i][j]))
            elif i >= ROWS or j >= COLS:
                return True
            else:
                return False

        cells = []
        for i in range(ROWS):
            for j in range(COLS):
                visit = set()
                atlantic = can_atlantic(i, j, heights[i][j])

                visit = set()
                pacific  = can_pacific(i, j, heights[i][j])
                if atlantic and pacific:
                    cells.append([i,j])

        return cells