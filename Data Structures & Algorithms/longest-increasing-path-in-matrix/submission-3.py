from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def run(i, j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            if matrix[i][j] > prev:
                return 1 + max(run(i+1, j, matrix[i][j]) , run(i, j+1, matrix[i][j]) , run(i-1, j, matrix[i][j]) , run(i, j-1, matrix[i][j]))
            else:
                return 0

        max_len = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_len = max(max_len, run(i, j, -1))

        return max_len