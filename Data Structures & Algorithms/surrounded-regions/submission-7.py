class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def is_surrounded(i, j):
            if i>=0 and j>=0 and i<ROWS and j<COLS and (i,j) not in visit:
                visit.add((i, j))
                if board[i][j]=='X':
                    return True
                elif board[i][j]=='O' and i>0 and j>0 and i<ROWS-1 and j<COLS-1:
                    return True and is_surrounded(i+1, j) and is_surrounded(i-1, j) and is_surrounded(i, j+1) and is_surrounded(i, j-1)
                elif board[i][j]=='O' and (i==0 or j==0 or i==ROWS-1 or j==COLS-1):
                    return False
            else:
                return True

        for i in range(1, ROWS-1):
            for j in range(1, COLS-1):
                if board[i][j] == 'O':
                    visit = set()
                    if is_surrounded(i, j):
                        for visited in visit:
                            i2, j2 = visited
                            board[i2][j2] = 'X'
                    else:
                        pass


