class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price  = max(prices)
        max_profit = -1
        for price in prices:
            if price < min_price:
                min_price = price
            if max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit
        