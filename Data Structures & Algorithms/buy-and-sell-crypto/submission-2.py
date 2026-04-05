class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(1, len(prices)):
            sell_at = prices[i]
            buy_at = min(prices[:i])

            profit = sell_at - buy_at

            if profit >= max_profit:
                max_profit = profit
        return max_profit

        