class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sNums = set()

        for num in nums:
            sNums.add(num)
        
        best = 0
        for num in nums:
            cur = 1
            lookup = num + 1
            while lookup in sNums:
                cur += 1
                lookup += 1
            if cur > best:
                best = cur
        return best
