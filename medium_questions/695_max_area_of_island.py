class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Iterate through graph and perform dfs
        return sum of all around
        maintain max area
        """
        self.res = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = dfs(r, c)
                self.res = max(self.res, area)

        return self.res
        
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Do bfs with queue
        For every 1 increment count
        """

        def helper(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            
            right = helper(r+1, c)
            left = helper(r-1, c)
            down = helper(r, c+1)
            up = helper(r, c-1)
            
            return right + left + down + up + 1
            


        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(helper(r, c), res)
        return res
        