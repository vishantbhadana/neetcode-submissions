class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            if prices[i]<buy:
                buy=prices[i]
            profit = max(profit, (sell-buy))

        return profit



    
        