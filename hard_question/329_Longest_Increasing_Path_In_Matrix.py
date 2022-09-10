class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        1. Do bfs on each node
        2. Keep visited set to avoid cycles
        """
        
        res = 1
        visited = {}
        
        def dfs(i, j, cur):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= cur:
                return 0
            if (i,j) in visited:
                return visited[(i,j)]
            r = 1
            up = dfs(i-1, j, matrix[i][j])
            down = dfs(i+1, j, matrix[i][j])
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])
            r = max(r, up + 1, down+ 1, left+ 1, right+ 1)
            visited[(i,j)] = r
            return r
            
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j, float("-inf")))
                
        return res