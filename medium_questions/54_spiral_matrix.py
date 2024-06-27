from typing import List
import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        layers = math.ceil(min(ROWS, COLS) / 2)
        
        res = []

        for l in range(layers):
            width = COLS - 2 * l
            height = ROWS - 2 * l

            # Top row
            for i in range(l, l + width):
                res.append(matrix[l][i])
            
            # Right col
            for i in range(l + 1, l + height):
                res.append(matrix[i][l + width - 1])
            
            # Bot row (only if not the same as top row)
            if height > 1:
                for i in range(l + width - 2, l - 1, -1):
                    res.append(matrix[l + height - 1][i])

            # Left col (only if not the same as right col)
            if width > 1:
                for i in range(l + height - 2, l, -1):
                    res.append(matrix[i][l])
        
        return res
