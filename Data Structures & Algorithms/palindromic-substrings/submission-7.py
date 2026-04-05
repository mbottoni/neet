import functools
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        possibles = []
        @functools.cache
        def dfs(i, j):
            if i>=0 and j<n:
                if s[i]==s[j]:
                    possibles.append(s[i:j+1])
                    dfs(i-1, j+1)
                else:
                    return
            else:
                return

        for i in range(n):
            dfs(i, i)
            dfs(i, i+1)

        #print(possibles)
        return len(possibles)
                    
        