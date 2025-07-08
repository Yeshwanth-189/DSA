class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Brute force Approach
        max_profit=0
        profit=0
        for buy_day in range(len(prices)):
            for sell_day in range(buy_day+1,len(prices)):
                profit=prices[sell_day]-prices[buy_day]
                if profit>max_profit:
                    max_profit=profit
        return max_profit"""

        min_price_so_far=float('inf')
        max_profit=0
        profit=0
        for i in range(len(prices)):
            if prices[i]<min_price_so_far:
                min_price_so_far=prices[i]
            profit=prices[i]-min_price_so_far
            if profit>max_profit:
                    max_profit=profit
        return max_profit

        
        