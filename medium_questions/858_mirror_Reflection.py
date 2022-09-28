class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        Number of reflections to reach a corner 
        
        (q * (n)) = p
        
        p = 3
        q = 1
        
        1 * (n) = 3
        n = 3
        
        
        
        number of q required to reach a corner is n
        
        n*q = where ray meets corner 
        
        if n is even:
            going to hit left side so 2
            
        if n is odd:
            squares = n*q // p 
            if square odd:
                return 0
            even:
                return 1
            
        p*x % q*n = 0
        
        where x is minimum integer

        """
        
        """
        
            
        """   
        def helper(x, y):
            if x > y:
                z = x
            else:
                z = y
            while(True):
                if((z % x == 0) and (z % y == 0)):
                    lcm = z
                    break
                z += 1
            return lcm
        
        n = helper(p, q)
        n = n // q
        if n%2 == 0:   
            return 2
        else:
            squares = n*q // p
            print(n*q // p)
            if squares % 2 == 0:
                return 0
            else:
                return 1