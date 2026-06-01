class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #set to map row/column/box
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":  #skips mapping "."
                    continue
                
                r = (i // 3) * 3 + (j // 3)
                if val in row[i] or val in col[j] or val in box[r]:
                    return False
            
                row[i].add(val)
                col[j].add(val)
                box[r].add(val)
        
        return True


                
        