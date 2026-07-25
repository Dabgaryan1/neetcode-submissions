class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        i, j = 0, len(s1) - 1
        compare = [0] * 26
        freq = [0] * 26

        for k in range(len(s1)):
            compare[ord(s1[k]) - ord('a')] += 1
            freq[ord(s2[k]) - ord('a')] += 1

        if compare == freq:
            return True

        while j + 1 < len(s2):
            # Remove the character leaving the window
            freq[ord(s2[i]) - ord('a')] -= 1
            i += 1

            # Add the character entering the window
            j += 1
            freq[ord(s2[j]) - ord('a')] += 1

            if compare == freq:
                return True

        return False