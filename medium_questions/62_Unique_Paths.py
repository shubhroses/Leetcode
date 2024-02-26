class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic = {}
        def helper(i, j):
            if i == 1 or j == 1:
                return 1
            if i == 0 or j == 0:
                return 0
            if (i, j) in dic:
                return dic[(i, j)]
            else:
                dic[(i, j)] = helper(i-1, j) + helper(i, j-1)
                return dic[(i,j)]
        return helper(m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Starting at start, can go down or left
        If out of bounds return 0
        if reach finish return 1
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        print(dp)

        for r in range(m):
            dp[r][n-1] = 1
        for c in range(n):
            dp[m-1][c] = 1
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            memo[(r, c)] = helper(r+1, c) + helper(r, c+1)
            return memo[(r, c)]
        return helper(0, 0)
