class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        best = 0
        freq = defaultdict(int)
        for j in range(len(s)):
            freq[s[j]] += 1
            most = max(freq.values())

            while (j - i + 1) - most > k:
                if s[i] != max(freq.values()):
                    freq[s[i]] -= 1
                i += 1
            best = max(best, j - i + 1)
        return best




        