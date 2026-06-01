class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zeros = 0
        count = 1

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                count *= num

        if zeros > 1:
            return [0] * len(nums)

        if zeros > 0:
            for num in nums:
                if num == 0:
                    output.append(count)
                else:
                    output.append(0)
            return output
        
        for num in nums:
            output.append(int(count/num))
        return output

        


            
        