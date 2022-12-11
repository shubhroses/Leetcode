class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        [1,2,4]
        [3,3,1]
        
        [1, 2, 4]
        [1, 3, 3]
        
        res = 0
        
        res += max(4, 3)
        
        4 -> 3 -> 1 = 8
        
        
        """
        for i in range(len(grid)):
            grid[i] = sorted(grid[i], reverse = True)
        
        res = 0
        for j in range(len(grid[0])):
            res += max([row[j] for row in grid])
        return res
                   