class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        1. For any point: choose a direction and see if the values are the same
        2. If the length of same letters chain is of size >= 3, save that position to be deleted
        3. Iterate through all positions and call delete function which move all elements above one down. 
        4. Repeat whole process until set to be deleted is empty
        """
        toDelete = set()
        
        def sameDir(i,j, cur, direction):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 0
            if board[i][j] == 0 or board[i][j] != cur:
                return 0
            if direction == "up":
                return sameDir(i-1, j, cur, direction) + 1
            if direction == "down":
                return sameDir(i+1, j, cur, direction) + 1
            if direction == "left":
                return sameDir(i, j-1, cur, direction) + 1
            if direction == "right":
                return sameDir(i, j+1, cur, direction) + 1
        
        def markToDelete(i, j):
            up = sameDir(i-1, j, board[i][j], "up")
            down = sameDir(i+1, j, board[i][j], "down")
            left = sameDir(i, j-1, board[i][j], "left")
            right = sameDir(i, j+1, board[i][j], "right")
            
            if up + down + 1 >= 3:
                for x in range(i-up, i+down+1):
                    toDelete.add((x, j))
            if left + right + 1 >= 3:
                for y in range(j-left, j+right+1):
                    toDelete.add((i,y))
        
        def deleteMarked(i,j):
            for x in range(i, 0, -1):
                board[x][j] = board[x-1][j]
            board[0][j] = 0
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                markToDelete(i, j)
                
        while len(toDelete) > 0:
            for i,j in toDelete:
                board[i][j] = '#'

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        deleteMarked(i,j)
            toDelete.clear()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    markToDelete(i, j)
        return board
        

        class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board
        
        
        """
        1. For any point: choose a direction and see if the values are the same
        2. If the length of same letters chain is of size >= 3, save that position to be deleted
        3. Iterate through all positions and call delete function which move all elements above one down. 
        4. Repeat whole process until set to be deleted is empty
        """
        toDelete = set()
        
        def sameDir(i,j, cur, direction):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 0
            if board[i][j] == 0 or board[i][j] != cur:
                return 0
            if direction == "up":
                return sameDir(i-1, j, cur, direction) + 1
            if direction == "down":
                return sameDir(i+1, j, cur, direction) + 1
            if direction == "left":
                return sameDir(i, j-1, cur, direction) + 1
            if direction == "right":
                return sameDir(i, j+1, cur, direction) + 1
        
        def markToDelete(i, j):
            up = sameDir(i-1, j, board[i][j], "up")
            down = sameDir(i+1, j, board[i][j], "down")
            left = sameDir(i, j-1, board[i][j], "left")
            right = sameDir(i, j+1, board[i][j], "right")
            
            if up + down + 1 >= 3:
                for x in range(i-up, i+down+1):
                    toDelete.add((x, j))
            if left + right + 1 >= 3:
                for y in range(j-left, j+right+1):
                    toDelete.add((i,y))
        
        def deleteMarked(i,j):
            for x in range(i, 0, -1):
                board[x][j] = board[x-1][j]
            board[0][j] = 0
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                markToDelete(i, j)
                
        while len(toDelete) > 0:
            for i,j in toDelete:
                board[i][j] = '#'

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        deleteMarked(i,j)
            toDelete.clear()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    markToDelete(i, j)
        return board
        