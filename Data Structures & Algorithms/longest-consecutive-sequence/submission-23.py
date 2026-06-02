class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sNums = set()

        for num in nums:
            sNums.add(num)
        
        best = 0
        for num in nums:
            if num - 1 not in sNums:
                cur = 1
                lookup = num + 1
                while lookup in sNums:
                    cur += 1
                    lookup += 1
                best = max(cur, best)
        return best
