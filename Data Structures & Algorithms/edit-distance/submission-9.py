from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #@cache
        from collections import defaultdict
        dp = defaultdict(int)
        def run(i, j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i

            if (i,j) in dp:
                return dp[(i,j)]

            if word1[i] == word2[j]:
                return run(i+1, j+1)
            else:
                insert = 1 + run(i, j+1)
                delete = 1 + run(i+1, j)
                replace = 1 + run(i+1, j+1)
                result = min(insert, delete, replace)
                dp[(i,j)] = result
                return dp[(i,j)]

        return run(0,0)
                

        