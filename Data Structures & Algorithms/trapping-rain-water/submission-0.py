class Solution:
    def trap(self, height: List[int]) -> int:
        solution = 0

        i = 0;
        j = len(height)-1
        
        Lmax = height[i]
        Rmax = height[j]

        while i < j:
            if height[i] <= height[j]:
                water = min(Lmax,Rmax) - height[i]
                if water < 1:
                    solution += 0
                else:
                    solution += water
                i += 1
                if height[i] >= Lmax:
                    Lmax = height[i]
            else:
                water = min(Lmax,Rmax) - height[j]
                if water < 1:
                    solution += 0
                else:
                    solution += water
                j -= 1
                if height[j] >= Rmax:
                    Rmax = height[j]
        return solution