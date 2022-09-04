class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Start at all borders
        run dfs turning to x

        """
        def dfs(i,j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == "O":
                board[i][j] = "Y"
                
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            return
                
        
        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)
            
        for i in range(1, len(board[0])-1):
            dfs(0,i)
            dfs(len(board)-1, i)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Y":
                    board[i][j] = "O"