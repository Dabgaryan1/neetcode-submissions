class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        map = {}
        arr = []

        for index, value in enumerate(nums):
            map[value] = index
        
        for index, value in enumerate(nums):
            difference = target - value
            if difference in map and map[difference] != index:
                return sorted([map[difference], index])
                
        

        

        