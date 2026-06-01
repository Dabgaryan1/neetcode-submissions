class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)] #create a pair array of (pos, speed)
        stack = []  #stack to find collisions

        for p, s in sorted(pair)[::-1]: #traverse through SORTED pair array in REVERSE order
            stack.append((target - p) / s)  #append the time it will take to reach target for each p,s
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  #remove collisions from stack 
                stack.pop()                                 #by comparing top with 2nd to top item in stack
        return len(stack)       #return length of stack

