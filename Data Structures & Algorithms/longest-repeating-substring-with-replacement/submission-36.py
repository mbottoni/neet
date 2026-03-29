class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substr = 0
        left, right = 0, 0
        from collections import defaultdict
        d = defaultdict(int)
        d[s[left]] += 1
        while left < len(s) and right < len(s):
            substr = s[left:right+1]
            if abs(len(substr) - max(d.values())) <= k:
                max_substr = max(max_substr, right - left + 1)
                right += 1
                if right < len(s):  # Fix 3: guard before accessing s[right]
                    d[s[right]] += 1
            else:
                d[s[left]] -= 1
                left += 1

        return max_substr