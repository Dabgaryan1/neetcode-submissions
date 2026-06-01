class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        map = {}

        for key, value in enumerate(nums):
            g = target - value
            
            if g in map:
                res.append(map[g])
                res.append(key)
                break
            map[value] = key
        return res