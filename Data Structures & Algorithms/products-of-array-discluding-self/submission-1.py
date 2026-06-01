class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zeroCount = 0

        #find total product of all integers in List not including 0's
        totalProduct = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            else:
                totalProduct *= num
        
        #edge case for multiple 0's
        if zeroCount > 1:
            for num in nums:
                output.append(num * 0)
            return output

        for num in nums:
            if num == 0:
                output.append(totalProduct)
            elif num != 0 and zeroCount == 1:
                output.append(0)
            else:
                output.append(int(totalProduct / num))
        
        return output
            
        



