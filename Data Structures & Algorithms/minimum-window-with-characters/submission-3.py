from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def to_dict(s):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            return d

        def cond(d1, base):
            for key in base.keys():
                if base[key] > d1[key]:
                    return False
            return True

        dict_t = to_dict(t)
        s_t = defaultdict(int)
        left = 0
        substr = ""

        for right in range(len(s)):         # expand right edge
            s_t[s[right]] += 1
            while cond(s_t, dict_t):        # shrink left edge while valid
                window = s[left:right + 1]
                if not substr or len(window) < len(substr):
                    substr = window
                s_t[s[left]] -= 1
                left += 1

        return substr