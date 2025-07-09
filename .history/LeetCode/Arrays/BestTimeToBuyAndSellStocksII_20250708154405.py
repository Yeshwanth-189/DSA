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

        