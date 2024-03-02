class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Starting at each point
        Maintain a prev

        When element is <= prev: return 0
        if index is out of bounds return 0
        if in path visited: return 0
        if element > prev: return all 4 directions + 1
        """
        dp = {}
        def helper(r, c, prev, visited):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0
            if matrix[r][c] <= prev or (r, c) in visited:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            visited.add((r, c))

            down = helper(r+1, c, matrix[r][c], visited)
            up = helper(r-1, c, matrix[r][c], visited)
            right = helper(r, c+1, matrix[r][c], visited)
            left = helper(r, c-1, matrix[r][c], visited)
            visited.remove((r, c))
            dp[(r, c)] = max(up, down, left, right) + 1
            return dp[(r, c)]

        res = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                visited = set()
                res = max(res, helper(r, c, -1, visited))
        return res
