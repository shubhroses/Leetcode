class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
            else:
                return
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            helper(r+1, c)
            helper(r-1, c)
            helper(r, c+1)
            helper(r, c-1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    helper(r, c)
                    res += 1
        return res
