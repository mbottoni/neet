class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def run(i, j):
            if i == len(s) and j == len(p):
                return True
            elif i == len(s) and j < len(p):
                # remaining pattern must be skippable (e.g. "a*b*")
                return j + 1 < len(p) and p[j+1] == '*' and run(i, j+2)
            elif i < len(s) and j == len(p):
                return False

            if j + 1 < len(p) and p[j+1] == '*':  # look-ahead for '*'
                # option 1: skip the "x*" pair
                # option 2: use it if current chars match
                return run(i, j+2) or (
                    (p[j] == '.' or p[j] == s[i]) and run(i+1, j)
                )
            elif p[j] == '.' or p[j] == s[i]:  # fix
                return run(i+1, j+1)
            else:
                return False

        return run(0, 0)