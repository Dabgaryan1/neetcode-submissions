class Solution:
    def isValid(self, s: str) -> bool:
        
        k = []

        for c in s:
            if c == '(' or c == '[' or c == '{':    #pushes opening brackets into stack
                k.append(c)

            if not k:
                return False
            #check if closing brackets match corresponding opening bracket 
            if c == ')':
                if k[-1] == '(':
                    k.pop()
                    continue
                return False    
            if c == ']':
                if k[-1] == '[':
                    k.pop()
                    continue
                return False
            if c == '}':
                if k[-1] == '{':
                    k.pop()
                    continue
                return False
        
        return True if not k else False