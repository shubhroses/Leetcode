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