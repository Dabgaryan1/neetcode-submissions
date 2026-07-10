class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        while left <= right:
            m = (left + right) // 2
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[m]) - 1]:
                #binary search this row
                l, r = 0, len(matrix[m]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target == matrix[m][mid]:
                        return True
                    elif target < matrix[m][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            elif target < matrix[m][0]:
                right = m - 1
            else:
                left = m + 1
        return False
