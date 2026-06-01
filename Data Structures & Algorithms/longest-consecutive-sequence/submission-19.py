class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxCount = 1   #output
        nums = set(nums)
        
        curr = 0
        for num in sorted(nums):
            curr += 1
            if num + 1 in nums:
                continue
            else:
                if curr > maxCount:
                    maxCount = curr
                curr = 0
        return maxCount





