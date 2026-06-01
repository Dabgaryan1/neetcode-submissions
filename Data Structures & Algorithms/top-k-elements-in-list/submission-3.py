class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        for num in sorted(map, key = map.get):
            if len(map) == k:
                break
            else:
                del map[num]
        return list(map.keys())