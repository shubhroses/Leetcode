class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Start dfs at edge nodes
        Maintain sets of can be reached by pacific and atlantic
        """
        pacific = set()
        atlantic = set()


        def dfs(r, c, visited, prev):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            if heights[r][c] < prev:
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])


        # left and right
        for r in range(len(heights)):
            dfs(r, 0, pacific, -1)
            dfs(r, len(heights[0])-1, atlantic, -1)
        
        # top and bottom
        for c in range(len(heights[0])):
            dfs(0, c, pacific, -1)
            dfs(len(heights)-1, c, atlantic, -1)
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
