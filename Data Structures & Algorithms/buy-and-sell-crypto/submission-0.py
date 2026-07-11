class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, value in enumerate(prices):
            pointer = i+1
            while pointer < len(prices):
                maxProfit = max(maxProfit, prices[pointer]-value)
                pointer +=1
        return maxProfit
        