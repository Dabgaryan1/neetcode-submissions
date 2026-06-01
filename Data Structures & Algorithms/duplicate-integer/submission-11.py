class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        numbers = defaultdict(int)

        for num in nums:
            numbers[num] += 1
        
        if max(numbers.values()) > 1: 
            return True
        return False