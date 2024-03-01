class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3): return False
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            dp[(i, j)] = False
            return False
        return dfs(0, 0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Maintain l and r and t pointers for each string
        If s3[t] == s1[l] and s3[t] == s2[r]:
            then take left and take right
        elif s3[t] == s1[l]:
            take left
        elif s3[t] == s2[r]:
            take right:
        else:
            return 0
        if reach end of s3 and end of s2 and end of s1 then return 
        if reach end of s1 and s2 but not s3, return 0
        if reach end of s3 but not s1 or s2 return 0
        else return 0
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]


        memo = {}
        def helper(l, r, t):
            if (l, r, t) in memo:
                return memo[(l, r, t)]
            if t == len(s3) and l == len(s1) and r == len(s2):
                return 1
            elif (t == len(s3)) or (l == len(s1) and r == len(s2)):
                return 0
            if l < len(s1) and r < len(s2) and s3[t] == s1[l] and s3[t] == s2[r]:
                left = helper(l+1, r, t+1)
                right = helper(l, r+1, t+1)
                memo[(l, r, t)] = left + right
            elif l < len(s1) and s3[t] == s1[l]:
                memo[(l, r, t)] = helper(l+1, r, t+1)
            elif r < len(s2) and s3[t] == s2[r]:
                memo[(l, r, t)] = helper(l, r+1, t+1)
            else:
                memo[(l, r, t)] = 0
            return memo[(l, r, t)]
        return helper(0, 0, 0)
            
