class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        self.res = []

        board = [["."]*n for _ in range(n)]

        def backtracking(r):
            if r == n:
                self.res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                board[r][c] = 'Q'

                backtracking(r+1)

                cols.remove(c)
                posDiag.remove((r+c))
                negDiag.remove((r-c))
                board[r][c] = '.'

        backtracking(0)

        return self.res