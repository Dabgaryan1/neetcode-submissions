class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)

        best = 0
        for num in snums:
            if num - 1 in snums:
                continue
            cur = 1
            g = num
            while g + 1 in snums:
                cur += 1
                g += 1
            best = max(cur, best)
        return best