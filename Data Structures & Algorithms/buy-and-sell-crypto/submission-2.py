class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestBuy = prices[0]
        for i in range(1,len(prices)):
            if(prices[i] < bestBuy):
                bestBuy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - bestBuy)  

        return maxProfit 