class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        hash_col = defaultdict(list)
        hash_row = defaultdict(list)
        hash_squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    hash_row[i] = hash_row[i] + [int(board[i][j])]
                    hash_col[j] = hash_col[j] + [int(board[i][j])]
                    hash_squares[(i // 3) * 3 + (j // 3)] = hash_squares[(i // 3) * 3 + (j // 3)] + [int(board[i][j])]

        for dicts in [hash_col, hash_row, hash_squares]:
            for key in dicts:
                if len(dicts[key]) != len(set(dicts[key])):
                    return False
                    
        return True
