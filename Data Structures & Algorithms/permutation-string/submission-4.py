from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def to_dict(s): # O(n)
            d = defaultdict(int)
            for i in range(len(s)):
                d[s[i]] += 1
            return d
    


        s1_d = to_dict(s1)
        print(s1_d)
        for i in range(0, len(s2)-len(s1)+1):
            s2_d = to_dict(s2[i:i+len(s1)])
            print(s2_d)
            if s2_d == s1_d:
                return True

        return False
        