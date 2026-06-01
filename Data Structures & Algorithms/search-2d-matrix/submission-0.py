class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            k = 0
            j = len(matrix[i]) - 1
            while k <= j:
                m = (j+k) // 2
                if target > matrix[i][m]:
                    k = m + 1
                elif target < matrix[i][m]:
                    j = m - 1
                else:
                    return True
        return False
            