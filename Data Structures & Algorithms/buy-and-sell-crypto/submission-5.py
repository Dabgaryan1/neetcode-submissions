class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 #stores current best profit
        i, j = 0, 1

        while i < len(prices):
            if j < len(prices) and prices[i] >= prices[j]:
                i += 1
                j += 1
                continue
            while j < len(prices) and prices[j] > prices[i]:
                best = max(best, prices[j]-prices[i])
                j += 1
            i = j
            j += 1
        return best

            
        