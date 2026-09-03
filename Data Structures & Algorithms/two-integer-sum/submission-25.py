class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, j in enumerate(nums):
            g = target - j
            if g in m:
                return [m[g], i]
            m[j] = i
            
        