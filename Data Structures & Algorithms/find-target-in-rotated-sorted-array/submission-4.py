class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] == target: 
                return m
            if nums[m] >= nums[i]:
                if target > nums[m] or target < nums[i]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                if target < nums[m] or target > nums[j]:
                    j = m - 1
                else:
                    i = m + 1
        return -1
                
