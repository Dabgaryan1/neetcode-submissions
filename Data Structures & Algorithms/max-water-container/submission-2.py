class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestSize = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            width = j - i
            if heights[i] > heights[j]:
                curSize = heights[j] * width
                j -= 1
            else:
                curSize = heights[i] * width
                i += 1   
            if curSize > bestSize:
                bestSize = curSize

        return bestSize