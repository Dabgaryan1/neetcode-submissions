class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        
        for s in strs:
            mapping = [0] * 26

            for c in s:
                mapping[ord(c) - ord('a')] += 1
            grouping[tuple(mapping)].append(s)
        return list(grouping.values())