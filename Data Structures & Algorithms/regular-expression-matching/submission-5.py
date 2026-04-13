from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def run(i, j):
            # base cases
            if i == len(s) and j == len(p):
                return True
            if i == len(s):
                return j + 1 < len(p) and p[j + 1] == '*' and run(i, j + 2)
            if j == len(p):
                return False

            # look ahead: next pattern char is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                skip_pair    = run(i, j + 2)
                use_wildcard = (p[j] == '.' or p[j] == s[i]) and run(i + 1, j)
                return skip_pair or use_wildcard

            # literal or '.' match
            if p[j] == '.' or p[j] == s[i]:
                return run(i + 1, j + 1)

            return False

        return run(0, 0)