class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        i = 0
        chars = set()
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            best = max(best, j-i + 1)
            chars.add(s[j])
        return best