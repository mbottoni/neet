from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def run(i, j):
            if i == len(word1): return len(word2)-j
            if j == len(word2): return len(word1)-i
            if word1[i] == word2[j]:
                return run(i+1, j+1)
            else:
                insert = 1 + run(i, j+1)
                delete = 1 + run(i+1, j)
                replace = 1 + run(i+1, j+1)
                return min(insert, delete, replace)
        return run(0,0)
                

        