class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        i = 0
        j = 0
        cur = ""

        while i < len(s):
            if j >= len(s):
                if len(cur) > best:
                    best = len(cur)
                break
            

            if s[j] in cur:
                i += 1
                j = i
                if len(cur) > best:
                    best = len(cur)
                cur = ""
            else:
                cur += s[j]
                j += 1
        return best

                


