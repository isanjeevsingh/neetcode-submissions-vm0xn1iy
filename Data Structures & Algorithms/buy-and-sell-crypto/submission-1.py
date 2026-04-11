class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             max_profit = max(max_profit, prices[j]-prices[i])
        # return max_profit
        
        low = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p < low:
                low = p
            else:
                max_profit = max(max_profit, p-low)
        return max_profit
