class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        best = most
        k = 1
        while k <= most:
            mid = (k + most) // 2
            
            cur = 0
            for p in piles:
                cur += math.ceil(p / mid)
            if cur <= h:
                best = min(best, mid)
                most = mid - 1
            else:
                k = mid + 1
        return best