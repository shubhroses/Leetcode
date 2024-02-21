
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Need to find number of ways to decode a string

        If at last digit and digit is 0 return 0 else 1
        If digit starts with 1 or 2 have option to take 1 or 2 digits
        """
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            takeOne = dfs(i + 1)
            takeTwo = 0
            if i < len(s) - 1:
                if s[i] == "1":
                    takeTwo = dfs(i+2)
                elif s[i] == "2" and int(s[i + 1]) <= 6:
                    takeTwo = dfs(i+2)
            memo[i] = takeOne + takeTwo
            return memo[i]

        return dfs(0)
    

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Need to find number of ways to decode a string

        If at last digit and digit is 0 return 0 else 1
        If digit starts with 1 or 2 have option to take 1 or 2 digits
        """
        # Dynamic Programming
        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i < len(s) - 1:
                if s[i] == "1":
                    dp[i] += dp[i+2]
                elif s[i] == "2" and s[i+1] in "0123456":
                    dp[i] += dp[i+2]
        return dp[0]
        """
        Just add whats to the right, and if satisfies situation of a two digits add what two to the right
        """

