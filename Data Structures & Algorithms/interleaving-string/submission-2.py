from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def run(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res = res or run(i+1, j, k+1)
            if j < len(s2) and s3[k] == s2[j]:
                res = res or run(i, j+1, k+1)
            return res
    
        return run(0, 0, 0)