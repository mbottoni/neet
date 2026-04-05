class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = []

        def dfs(i, j):
            if i >= 0 and j < n:
                if s[i] == s[j]:
                    max_len.append(s[i:j+1])  # append before recursing
                    dfs(i-1, j+1)
                else:
                    return
            else:
                return

        for mid in range(n):
            dfs(mid, mid)
            dfs(mid, mid+1)  # even-length palindromes

        return max(max_len, key=len)