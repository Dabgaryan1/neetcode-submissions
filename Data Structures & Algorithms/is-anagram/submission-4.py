class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list = []

        for char in s:
            list.append(char)
        
        for char in t:
            if char in list:
                list.remove(char)
        
        if not list:
            return True
        else:
            return False
