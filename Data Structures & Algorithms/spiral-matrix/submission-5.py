class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        moves = {0: (0,1), 1: (1,0), 2: (0,-1), 3: (-1,0)}  # right, down, left, up
        vis = set()
        res = []

        def run(i, j, state):
            if len(res) == n * m:  # base case
                return
            if (i < 0 or i >= n or j >= m or j < 0) or (i,j) in vis:
                # switch direction
                move = moves[state]
                new_state = (state+1) % 4
                new_move = moves[new_state]
                run(i-move[0]+new_move[0], j-move[1]+new_move[1], state=new_state)
            else:
                # keep going 
                move = moves[state]
                res.append(matrix[i][j])
                vis.add((i,j))

                run(i+move[0], j+move[1], state)

        run(0, 0, 0)
        return res