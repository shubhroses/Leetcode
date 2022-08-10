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