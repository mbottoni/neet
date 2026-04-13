from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def run(i, state):
            if i >= len(prices):
                return 0

            if state == "free":
                buy    = -prices[i] + run(i + 1, "holding")  # spend money, now holding
                skip   = run(i + 1, "free")                   # do nothing
                return max(buy, skip)

            if state == "holding":
                sell   = prices[i] + run(i + 1, "cooldown")  # earn money, now in cooldown
                skip   = run(i + 1, "holding")                # hold on
                return max(sell, skip)

            if state == "cooldown":
                return run(i + 1, "free")                     # cooldown forces a skip

        return run(0, "free")