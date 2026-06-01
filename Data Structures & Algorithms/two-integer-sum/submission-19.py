class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        map = {}

        for i, key in enumerate(nums):
            g = target - key
            if g in map:
                list.append(map[g])
                list.append(i)
            map[key] = i
        return list