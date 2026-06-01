class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list = set(nums)    #turn nums into a set

        best = 0    #keep track of best amount
        curr = 1    #keep track of current amount

        for num in sorted(list):
            if num + 1 in list:
                curr += 1
                if curr > best:
                    best = curr
            else:
                if curr > best:
                    best = curr
                curr = 1
        return best

