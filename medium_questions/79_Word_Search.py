class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)
        P = len(word)
        
        def search(r,c,pos):
            if pos >= P:
                return True
            elif 0 <= r < height and 0 <= c < width and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if search(r+1,c,pos+1) or search(r-1,c,pos+1) or search(r,c+1,pos+1) or search(r,c-1,pos+1): 
                    return True
                board[r][c] = temp
        for r in range(height):
            for c in range(width):
                if search(r,c,0):
                    return True
        return False
        
         def helper(i, j, c):
            if c >= len(word):
                return True
            elif i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[c]:
                return False
            
            temp = board[i][j]
            board[i][j] = None
            if (helper(i-1, j, c+1) or \
               helper(i+1, j, c+1) or  \
               helper(i, j-1, c+1) or  \
               helper(i, j+1, c+1)):
                return True
            board[i][j] = temp
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False

        """
        word = ABC
               c
               
        if board[i][j] == word[c]
        
        call recursive on all adjacent neighbors with c += 1. 
        
        if c >= len(word)
        return True
        if i, j out of board return False
        
        and if i,j in path 
            return false
        
        after we have visited a node and returned false, take node out of path
        
        
        a b c
        s f c
        
        abfsa
            c
        
        path = {a, b, f, s}
        
        """
        
        def helper(i, j, suffix):
            if len(suffix) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != suffix[0]:
                return False
            
            board[i][j] = '#'
            res = (helper(i-1, j, suffix[1:]) or
                   helper(i+1, j, suffix[1:]) or 
                   helper(i, j-1, suffix[1:]) or 
                   helper(i, j+1, suffix[1:]))
            board[i][j] = suffix[0]
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, word):
                    return True
        return False
    
        # n * m to visit every position
        # call stack of dfs will be length of the word but since 4 directions it will be 4^n