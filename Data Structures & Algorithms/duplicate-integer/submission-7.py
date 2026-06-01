class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        return True if map.values() and max(map.values()) > 1 else False
