class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] = max(i, d[s[i]])

        size = 0
        end = d[s[0]]
        res = []
        for i in range(len(s)):
            c = s[i]
            end = max(end, d[c])  # extend end if needed
            size += 1

            if i == end:
                res.append(size)
                size = 0
                if i + 1 < len(s):
                    end = d[s[i+1]]

        return res