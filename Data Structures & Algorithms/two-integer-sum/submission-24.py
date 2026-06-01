class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for index, num in enumerate(nums):
            g = target - num
            if g in m:
                return [m[g], index]
            m[num] = index