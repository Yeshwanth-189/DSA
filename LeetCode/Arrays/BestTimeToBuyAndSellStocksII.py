class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        profit=0
        for i in range(n-1):
            if prices[i+1]-prices[i]>0:
                profit=prices[i+1]-prices[i]
                max_profit+=profit
        return max_profit
        

# This solution works by iterating through the prices and adding the profit whenever there is a price increase.
# It effectively captures all the upward movements in the stock prices, allowing for multiple transactions.        