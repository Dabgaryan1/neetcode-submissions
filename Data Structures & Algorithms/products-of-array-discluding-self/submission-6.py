class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocounter = 0
        solution = []
        product = 1

        for num in nums:
            if num == 0:
                zerocounter += 1
                continue
            product *= num
        
        #more than 1 zero
        if zerocounter > 1:
            for i in range(len(nums)):
                solution.append(0)
            return solution
        
        #1 zero
        if zerocounter == 1:
            for num in nums:
                if num == 0:
                    solution.append(product)
                else:
                    solution.append(0)
            return solution

        #no zeros
        for num in nums:
            solution.append(int(product/num))
        return solution
