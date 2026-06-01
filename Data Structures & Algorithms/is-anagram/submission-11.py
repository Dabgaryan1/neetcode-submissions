class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        
        a = sorted(s)
        b = sorted(t)

        if a == b:
            return True
        return False