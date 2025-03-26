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


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Starting at each node, we can do a dfs saving the length and dont visit visited nodes


        dfs:
            if out of bounds return 0
            if cur val <= prev val:
                return 0
            
            if r, c in visitedL
                return 0
            
            go in all 4 directions
            return max of those 4 directions

            remove from visited


        
        r, c = 0, 0
        res = 0
        visited = {(0, 0)}
        rev = -inf

        [[1,2]]


        if you are at a cell that has already been visited as a part of a longer path
        """
        res = 1
        self.visited = {}

        def dfs(r, c, prev):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= prev:
                return 0
            if (r, c) in self.visited:
                return self.visited[(r, c)]
            left = dfs(r-1, c, matrix[r][c])
            right = dfs(r+1, c, matrix[r][c])
            down = dfs(r, c+1, matrix[r][c])
            up = dfs(r, c-1, matrix[r][c])

            res = max(1, max(left, right, down, up) + 1)
            self.visited[(r, c)] = res
            return self.visited[(r, c)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c, float("-inf")))

        return res
