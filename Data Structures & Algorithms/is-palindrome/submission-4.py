class Solution:
    def isPalindrome(self, s: str) -> bool:
        String = ""

        for c in s:
            if c.isalnum():
                String += c.lower()

        i = 0
        j = len(String) - 1

        while i < j:
            if String[i] != String[j]:
                return False
            i += 1
            j -= 1
        return True