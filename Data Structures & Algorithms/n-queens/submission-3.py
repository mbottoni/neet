class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        cols, diag1, diag2 = set(), set(), set()

        def place(row, board):
            if row == n:
                sol.append(["".join(r) for r in board])
            else:
                for j in range(n):
                    if j in cols or (row-j) in diag1 or (row+j) in diag2:
                        continue
                    board[row][j] = 'Q'
                    cols.add(j); diag1.add(row-j); diag2.add(row+j)
                    place(row + 1, board)
                    board[row][j] = '.'
                    cols.remove(j); diag1.remove(row-j); diag2.remove(row+j)

        board = [['.' for _ in range(n)] for _ in range(n)]
        place(0, board)
        return sol