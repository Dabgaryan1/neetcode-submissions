class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        j = 1
        while i < len(prices) - 1:   
            if j >= len(prices):
                i += 1
                j = i + 1
                continue
            
            curProfit = prices[j] - prices[i]

            if curProfit > maxProfit:
                maxProfit = curProfit
            j += 1
        return maxProfit
