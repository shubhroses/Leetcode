class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        For all ones, maintain minX, maxX, minY, maxY
        return maxX - minX * maxY - minY


        [0,1,0]
        [1,0,1]

        (0, 1), (1, 0), (1, 2)

        minR = 0
        maxR = 1

        minC = 0
        maxC = 2

        area 3*2
        (maxC - minC + 1) * (maxR - minR + 1) 
        """

        minR, minC = float("inf"), float("inf")
        maxR, maxC = float("-inf"), float("-inf")

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    minR = min(minR, r)
                    maxR = max(maxR, r)
                    minC = min(minC, c)
                    maxC = max(maxC, c)
        return (maxC - minC + 1) * (maxR - minR + 1) 
