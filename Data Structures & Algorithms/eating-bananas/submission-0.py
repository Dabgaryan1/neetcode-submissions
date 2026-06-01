class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:
            k = (l + r) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / k)
            if count <= h:
                best = min(best, k)
                r = k - 1
            else:
                l = k + 1      
        return best