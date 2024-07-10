class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        Brute force, look at every submatrix 
        Go through each element and check if requirements
        If so add to res list

        tR, bR, lC, rC

        for r in range(tR, bR+1):
            for c in range(lC, rC+1):
                element = grid[r][c]
        Can use dp to store number of xs and ys 
        dp[r][c] should store the number of xs and ys in rectangle starting at origin
        """

        dp = [[[] for c in range(len(grid[0]))] for r in range(len(grid))]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                xCount, yCount = 0, 0
                if r > 0:
                    xCount += dp[r-1][c][0]
                    yCount += dp[r-1][c][1]
                if c > 0:
                    xCount += dp[r][c-1][0]
                    yCount += dp[r][c-1][1]
                if r > 0 and c > 0:
                    xCount -= dp[r-1][c-1][0]
                    yCount -= dp[r-1][c-1][1]
                if grid[r][c] == "X":
                    xCount += 1
                elif grid[r][c] == "Y":
                    yCount += 1
                dp[r][c] = [xCount, yCount]
        
        res = 0
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                xCount, yCount = dp[r][c]
                if xCount > 0 and xCount == yCount:
                    res += 1
        return res


