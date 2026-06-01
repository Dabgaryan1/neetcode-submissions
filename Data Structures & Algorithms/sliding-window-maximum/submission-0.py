class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        i = 0
        j = k-1
        while j < len(nums):
            res.append(max(nums[i:j + 1]))
            j += 1
            i += 1
        return res