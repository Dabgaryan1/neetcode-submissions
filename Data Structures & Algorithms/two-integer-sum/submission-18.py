class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        map = {}

        for i, key in enumerate(nums):
            g = target - key
            if g in map:
                res.append(map[g])
                res.append(i)
            map[key] = i
        return res