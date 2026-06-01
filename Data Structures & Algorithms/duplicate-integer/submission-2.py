class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []

        for num in nums:
            list.append(num)
        
        for num in nums:
            count = list.count(num)
            if count > 1:
                return True
        
        return False

        