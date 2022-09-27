class Solution:
    def minDays(self, n: int) -> int:
        
        saved = {}
        def helper(n):
            if n in saved:
                return saved[n]
            if n < 3:
                return n
            # n%2 or n%3 is the distance away n is from being divisible by 2 or 3 
            res = 1 + min(n%2 + helper(n//2), n%3 + helper(n//3))
            saved[n] = res
            return res
        return helper(n)
    """
    Want to each half so have to eat n % 2 before that is possible
    
    Want to each 2/3 so have to eat n % 2 before that is possible
    
    Are we trying to make it divisble by 2 or 3. Either way could reach minimum depending on number so try both branches. 
    
    
    """