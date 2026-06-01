class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map, s2map = defaultdict(int), defaultdict(int)

        # build counts for s1 and first window of s2
        for k in range(len(s1)):
            s1map[s1[k]] += 1
            s2map[s2[k]] += 1

        i = 0
        j = len(s1)

        while j < len(s2):
            if s1map == s2map:
                return True

            # slide window: remove left char
            s2map[s2[i]] -= 1
            if s2map[s2[i]] == 0:   # optional: keep dict clean
                del s2map[s2[i]]
            i += 1

            # add new right char
            s2map[s2[j]] += 1
            j += 1

        return s1map == s2map