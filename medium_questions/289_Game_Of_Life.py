class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        0 1 0
        0 0 1 -> 
        1 1 1
        
        c = cell
        n = number of neighbors
        
        if c == 1:
            if n < 2:
                c = 0
            elif n > 3:
                c = 0
            elif n == 2 or n == 3: #might not need this
                c = 1
        elif c == 0:
            if n == 3:
                c = 1
                
        Cant change board directly 
        Easy fix, save all changes in a set key = (x, y) 
        if a corrdinate is in a set, then flip its digit 
        
        n2 time and n2 space 
        
        maybe add 2 to each 
        """
        def helper(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 0
            return board[i][j]
        
        def count_neighbors(i, j):
            #return number of neighbors
            return helper(i-1, j) + helper(i+1, j) + helper(i, j-1) + helper(i, j+1) + helper(i-1, j-1) + helper(i-1, j+1) + helper(i+1, j-1) + helper(i+1, j+1)
            
            
        flip = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                n = count_neighbors(i, j)
                
                if c == 1:
                    if n < 2 or n > 3:
                        flip.add((i,j))
                elif c == 0:
                    if n == 3:
                        flip.add((i, j))
        
        for (i, j) in flip:
            if board[i][j] == 1:
                board[i][j] = 0
            else:
                board[i][j] = 1