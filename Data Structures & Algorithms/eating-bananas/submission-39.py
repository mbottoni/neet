import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            # Eat the bananas
            time = 0
            for p in piles:
                time+=math.ceil(float(p) / k)
            
            if time <= h:
                # We have a valid solution
                res = min(r, k)
                r = k-1
            else:
                l = k+1

        return res



