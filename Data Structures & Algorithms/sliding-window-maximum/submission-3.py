class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        sol = []
        while r < len(nums):
            sol.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return sol