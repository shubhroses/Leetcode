class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
         
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)
            
            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
            
            # Return the best option.
            return max(option_1, option_2)
                
        return memo_solve(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Starting at 0, 0 can move l or r one and compare
        If they are equal, move both, or move l or r
        """
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.res = 0
        def helper(l, r, cur):
            if l >= len(text1) or r >= len(text2):
                self.res = max(self.res, cur)
                return
            if text1[l] == text2[r]:
                helper(l+1, r+1, cur+1)
            helper(l+1, r, cur)
            helper(l, r+1, cur)
        helper(0, 0, 0)
        return self.res
