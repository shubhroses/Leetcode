class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        """
        Iterate through l, maintaining min prices

        Maintian res which is max cur pric - min price 

        [7,1,5,3,6,4] 
         L

         min = inf
         res = -inf
        
        min = min(min, l) 
        res = max(res, l - min)

        """
        res = float("-inf")
        curMin = float("inf")

        for ind, cost in enumerate(prices):
            curMin = min(curMin, cost)
            res = max(res, cost - curMin)

        return res
