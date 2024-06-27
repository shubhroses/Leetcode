class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        colsToZero = set()
        rowsToZero = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    colsToZero.add(c)
                    rowsToZero.add(r)
        
        for r in rowsToZero:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for c in colsToZero:
            for r in range(ROWS):
                matrix[r][c] = 0
        

        
