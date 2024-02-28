class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Create helper function
        index and canbuy

        if canBuy:
            buy
            skip
        
        if not canBuy:
            sell
            skip
        
        return max(buy, sell, skio)
        """
        dp = {}
        def helper(i, canBuy):
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            if i >= len(prices):
                return 0
            
            buy = sell = skip = 0
            skip = helper(i+1, canBuy)
            if canBuy:
                buy = helper(i+1, not canBuy) - prices[i]
            else:
                sell = helper(i+2, True) + prices[i]
            
            dp[(i, canBuy)] = max(buy, sell, skip)
            return dp[(i, canBuy)]
        return helper(0, True)