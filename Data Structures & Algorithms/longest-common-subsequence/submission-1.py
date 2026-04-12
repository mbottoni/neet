from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def run(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i]==text2[j]:
                return 1 + run(i+1, j+1)
            else:
                return max(run(i+1, j), run(i, j+1))

        return run(0, 0)
        