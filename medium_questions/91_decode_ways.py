
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
