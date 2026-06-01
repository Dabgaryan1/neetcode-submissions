class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        sortNums = sorted(nums)

        for i in range(len(sortNums)):
            target = 0 - sortNums[i]
            j = i + 1
            k = len(sortNums) - 1

            while j < k:
                if sortNums[j] + sortNums[k] < target:
                    j += 1
                elif sortNums[j] + sortNums[k] > target:
                    k -= 1
                else:
                    if [sortNums[i], sortNums[j], sortNums[k]] in res:
                        j += 1
                        k -= 1
                        continue
                    else:
                        res.append([sortNums[i],sortNums[j],sortNums[k]])
                        j += 1
                        k -= 1
                        
            i += 1
        return res