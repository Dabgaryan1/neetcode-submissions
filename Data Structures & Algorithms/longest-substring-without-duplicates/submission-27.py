class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0, 0
        best = 1

        while i < len(s):
            m = set()

            while j < len(s):
                if s[j] in m:
                    break
                else:
                    m.add(s[j])
                    j += 1
            best = max(best, j-i)
            i += 1
            j = i
        return best