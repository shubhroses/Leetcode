class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            ans = math.inf
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, helper(amount-coin)+1)
            dp[amount] = ans
            return ans
        ans = helper(amount)
        return ans if ans != math.inf else -1

        """
        1. Function to solve problem for a certain state
            At a given state need to know current total
            dp(amount) returns minimum coins needed for total remaining
        
        2. To tranition between states
            dp(total) = min(dp(amount-coin)+1) for all coins for all options 

        3. Base case
            if amount == 0 return 0
        """

        # Iterative solution
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != math.inf else -1