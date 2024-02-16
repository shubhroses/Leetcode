class Solution:
    def climbStairs(self, n: int) -> int:
        """
        
        3
        
        1st: 1
        2nd: 2
        3rd: 3
        4rd: 5
        """
        
        if n <= 1:
            return n
        x = 1
        y = 2
        cur = 2
        
        for i in range(2, n):
            cur = x + y
            x = y
            y = cur
        return cur

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)


        #edge cases
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]
        
