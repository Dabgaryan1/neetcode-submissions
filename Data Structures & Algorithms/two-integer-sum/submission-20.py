class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        map = {}

        for i, key in enumerate(nums):
            g = target - key
            if g in map:
                sol.append(map[g])
                sol.append(i)
            map[key] = i
        return sol 