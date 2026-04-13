from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def run(soma, i):
            if soma == amount:
                return 1
            if soma > amount or i == len(coins):
                return 0
            return run(soma + coins[i], i) + run(soma, i + 1)

        return run(0, 0)