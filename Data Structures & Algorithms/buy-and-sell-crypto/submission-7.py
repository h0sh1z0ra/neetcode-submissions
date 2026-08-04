class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        bestSell = 0

        while l < len(prices):
            for r in range(l,len(prices)):
                bestSell = max(bestSell, prices[r] - prices[l])
            l += 1
        
        return bestSell


