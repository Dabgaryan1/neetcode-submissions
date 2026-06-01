class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        sol = []

        for i, n in enumerate(nums):
            g = target - n
            if g in map:
                sol.append(map[g])
                sol.append(i)
                break
            map[n] = i
        return sol
            
