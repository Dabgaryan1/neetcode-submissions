class Solution:
    def isPalindrome(self, s: str) -> bool:
        noString = ""
        for c in s:
            if c.isalnum():
                noString += c
        
        print(noString)
        i = 0
        j = len(noString)-1

        while i < j:
            if noString[i].lower() != noString[j].lower():
                return False
            i += 1
            j -= 1
        return True

