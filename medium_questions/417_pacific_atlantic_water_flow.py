class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

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
