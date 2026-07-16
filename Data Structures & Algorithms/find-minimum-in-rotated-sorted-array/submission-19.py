class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = float('inf')
        
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        else:
            while l <= r:
                mid = (l + r) // 2
                
                sol = min(sol, nums[mid])
                if nums[l] <= nums[mid]:
                    sol = min(sol, nums[l])
                    l = mid + 1
                else:
                    r = mid - 1
        return sol

