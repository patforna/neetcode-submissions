class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # thoughts
        # - single scan from left to right
        # - keep track of cheapest seen so far
        # - check if seeling at current would max profit and keep track of max

        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
            

        