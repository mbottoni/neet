import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles) # FOr the binary search
        left, right = 1, max(piles)+1 # Speed of eating
        while left <= right:
            mid = (left+right)//2
            if sum([math.ceil(piles[j] / mid) for j in range(len(piles))]) <= h:
                # can finish on time, maybe can go slower?
                right = mid - 1
            else:
                # has to go faster
                left = mid + 1
        # Will leave the loop when left>right on this case false, false, true, true

        return left