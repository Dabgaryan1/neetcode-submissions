class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.sol = False

        def dfs(i, j, count):
            if i < 0 or i >= len(board):
                return

            if j < 0 or j >= len(board[i]):
                return

            if board[i][j] != word[count]:
                return

            tmp = board[i][j]
            board[i][j] = "#"
            if count == len(word) - 1:
                self.sol = True
                return

            dfs(i+1, j, count + 1)
            dfs(i-1, j, count + 1)
            dfs(i, j+1, count + 1)
            dfs(i, j-1, count + 1)
            board[i][j] = tmp
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, 0)
        return self.sol