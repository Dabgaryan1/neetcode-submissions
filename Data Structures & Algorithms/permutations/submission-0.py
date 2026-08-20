class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            if i >= len(nums):
                return
            
            for j in range(len(nums)):
                if nums[j] in cur:
                    continue
                cur.append(nums[j])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return res
