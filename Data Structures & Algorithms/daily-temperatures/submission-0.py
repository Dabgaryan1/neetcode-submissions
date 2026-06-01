class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) #default 0 array length of temperatures
        stack = []                       #empty stack to hold pair of value: index
        
        for i, j in enumerate(temperatures):    #iteratees through index, value
            while stack and j > stack[-1][0]:   #while the stack is not empty, and current value is greater than top stack value
                stackJ, stackInd = stack.pop()  # stackJ = popped stack value, stackInd = popped index
                result[stackInd] = (i-stackInd) #result at index stackInd set to current index - popped index    
            stack.append([j, i])    #appends current value and index to stack 
        return result           #returns result