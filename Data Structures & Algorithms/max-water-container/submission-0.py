class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestSize = 0
        curSize = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                width = j - i
                if heights[i] > heights[j]:
                    curSize = heights[j] * width
                else:
                    curSize = heights[i] * width

                if curSize > bestSize:
                    bestSize = curSize
        
        return bestSize

        
        