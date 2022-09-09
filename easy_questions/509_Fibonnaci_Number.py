class Solution:
    def fib(self, n: int) -> int:
        """
        fib(n) = fib(n-1) + fib(n-2)
        
        fib(4) = fib(3) + fib(2)
        
        fib(3) = fib(2) + fib(1)
        
        n=5
        x = 2
        y = 3
        
        cur = 5
        
        n = 4
        
        x = 1
        y = 2
        cur = 2
        
        i = 0     ...2
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        x = 0
        y = 1
        cur = 0
        
        for i in range(2, n+1):
            cur = x+y
            x = y
            y = cur
            
        return cur