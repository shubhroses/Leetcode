class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        """
        Go through each element in the grid and add to map {ord: (x, y)}
        Go through all elements in the set pair wise, make sure that every jump is possible
        
        """
        def isValid(x1, y1, x2, y2):
            if x1 == x2+1 and y1 + 2 == y2:
                return True
            elif x1 == x2+1 and y1 - 2 == y2:
                return True
            elif x1 == x2-1 and y1 - 2 == y2:
                return True
            elif x1 == x2-1 and y1 + 2 == y2:
                return True
            elif x1 == x2 + 2 and y1 == y2 + 1:
                return True
            elif x1 == x2 - 2 and y1 == y2 + 1:
                return True
            elif x1 == x2 - 2 and y1 == y2 - 1:
                return True
            elif x1 == x2 + 2 and y1 == y2 - 1:
                return True
            return False
        
        if grid[0][0] != 0:
            return False
        
        mp = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mp[grid[i][j]] = (i, j)
        
        n = len(grid)
        for x in range(1, n * n):
            prev = mp[x-1]
            cur = mp[x]
            if not isValid(prev[0], prev[1], cur[0], cur[1]):
                return False
        return True
            