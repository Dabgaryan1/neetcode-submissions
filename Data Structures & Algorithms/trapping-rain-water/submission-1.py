class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        i, j = 0, len(height) - 1
        Lmax, Rmax = height[i], height[j]
        total = 0

        while i < j:
            if Lmax < Rmax:
                i += 1
                Lmax = max(Lmax, height[i])
                total += Lmax - height[i] 
            else:
                j -= 1
                Rmax = max(Rmax, height[j])
                total += Rmax - height[j]
        return total