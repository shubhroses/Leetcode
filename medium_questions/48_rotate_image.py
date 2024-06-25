class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Save prev corner
        1 -> 7
        2 -> 4
        3 -> 1

        Go layer by layer


        1. Loop through layer, l
            n - 2
            
            1 -> 1
            2 -> 1
            3 -> 2
            4 -> 2
            5 -> 3
            6 -> 3

            l = (n / 2 round up) - 1
            length of side = n - 2 * l

            math.ceil(n/2)
            - Figure how the length of the side
            if l == 0: 
                side length = n
            if l == 1
                side length = n - 2
            if l == 2 
                side length = n - 2*l
        2. Iterate through each layer 
            bottom left = 0, n-1
            Set top left to bottom left
                r, c = 0, 0                     r, c = n-1, 0
            set top right to top left
                r, c = 0, n-1, 0.               r, c = 0, 0   
            set bottom right to top right
                r, c = n-1, n -1                r, c = 0, n-1
            set bottom left to bottom right
                r, c = 0, n-1                   r, c = n-1, n-1
        3. For i in range(l, l+length of side)
            swap 4
            bottom left = l, n-1-l
            Set top left to bottom left
                r, c = l, l+i                     r, c = n-1-l-i,l 
            set top right to top left
                r, c = l+i, n-1 -l                r, c = l, l+i  
            set bottom right to top right
                r, c = n-1-l, n -1-l-i             r, c = l+i, n-1-l
            set bottom left to bottom right
                r, c = n-1-l-i, l                  r, c = n-1-l, n-1-l-i
        """
        n = len(matrix)
        layers = math.ceil(n / 2)
        for l in range(layers):
            sideLen = n - 2 * l - 1
            for i in range(sideLen):
                topLeftRow, topLeftCol = l,l+i
                botLeftRow, botLeftCol = n-1-l-i,l
                botRighRow, botRighCol = n-1-l,n-1-l-i
                topRighRow, topRighCol = l+i,n-1-l

                savedTopLeft = matrix[topLeftRow][topLeftCol]
                matrix[topLeftRow][topLeftCol] = matrix[botLeftRow][botLeftCol]
                matrix[botLeftRow][botLeftCol] = matrix[botRighRow][botRighCol]
                matrix[botRighRow][botRighCol] = matrix[topRighRow][topRighCol]
                matrix[topRighRow][topRighCol] = savedTopLeft
