from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dfs(i):
            if i == len(s): return 1        # successfully decoded everything
            if s[i] == '0': return 0        # dead end
            ways = dfs(i+1)                 # take one digit
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)            # take two digits
            return ways
                
        
        return dfs(0)