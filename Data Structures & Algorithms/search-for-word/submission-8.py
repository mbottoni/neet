class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        cond = []

        def visit_regions(i, j, k):
            if k == len(word):
                cond.append(True)
                return
            if i >= 0 and j >= 0 and i < m and j < n:
                if board[i][j] == word[k]:          # match exact position, not substring
                    tmp, board[i][j] = board[i][j], "#"   # mark visited
                    visit_regions(i+1, j, k+1)
                    visit_regions(i-1, j, k+1)
                    visit_regions(i, j+1, k+1)
                    visit_regions(i, j-1, k+1)
                    board[i][j] = tmp                     # restore (backtrack)

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit_regions(i, j, 0)
        return any(cond)