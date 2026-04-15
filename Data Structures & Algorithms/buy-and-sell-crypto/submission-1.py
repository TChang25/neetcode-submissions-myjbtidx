class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currPrice = prices[0]
        currProfit = 0
        for i in range(len(prices)):
            if currPrice >= prices[i]:
                currPrice = prices[i]
            currProfit = max(currProfit, prices[i] - currPrice)
        return currProfit