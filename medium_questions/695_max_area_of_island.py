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