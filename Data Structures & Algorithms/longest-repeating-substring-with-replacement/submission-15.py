class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        map = defaultdict(int)  #maps character: frequency of character in string
        
        i = 0
        for j in range(len(s)):
            map[s[j]] += 1
            if ((j - i + 1) - max(map.values()) <= k):
                maxLength = max(maxLength, j - i + 1)
                j += 1
            else:
                map[s[i]] -= 1
                i += 1
        return maxLength

        