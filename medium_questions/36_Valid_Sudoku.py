class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Create a set
        for each element in row:
            if its a . continue
            make sure element not already in set
            make sure element >=1 <= 9
            add element to se

        """
        # Row check
        for row in board:
            elements = set()
            for element in row:
                if element == ".":
                    continue
                if element in elements:
                    return False
                if int(element) > 9 or int(element) < 1:
                    return False
                elements.add(element)
        
        # Column check
        for c in range(len(board[0])):
            elements = set()
            for r in range(len(board)):
                element = board[r][c]
                if element == ".":
                    continue
                if element in elements:
                    return False
                if int(element) > 9 or int(element) < 1:
                    return False
                elements.add(element)

        # Square check 
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                elements = set()
                for c in range(i, i+3):
                    for r in range(j, j+3):
                        element = board[r][c]
                        if element == ".":
                            continue
                        if element in elements:
                            return False
                        if int(element) > 9 or int(element) < 1:
                            return False
                        elements.add(element)
        return True