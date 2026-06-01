class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s))
            word += '%'
            for c in s:
                word += c
        return word
    def decode(self, s: str) -> List[str]:
        solution = []
        i = 0

        while i < len(s):
            c= ""
            while s[i] != '%':
                c += s[i]
                i += 1
            clen = int(c)

            j = i + 1
            end = j + clen
            tmp = ""
            while j < end:
                tmp += s[j]
                j += 1
            print(tmp)
            solution.append(tmp)
            i = j
        return solution

