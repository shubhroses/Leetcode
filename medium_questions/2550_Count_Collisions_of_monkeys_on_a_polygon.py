class Solution:
    def monkeyMove(self, n: int) -> int:
        """
        Total number of different positions
        
        each monkey can move left or right
        
        so its 2^n different positions
        
        How many of these position cause no collisions
        
        everyone moves to left, everyone moves to right
        
        If n is even, could pair up and swap 
        
        
        Lets say n is 3
        
        1. all left
        2. all right
        
        2^n - 2 = 2^3 - 3 = 8-2 = 6
        
        lets say n = 5
        
        1. all left
        2. all right
        3. 
        
        if n is odd return (2^n - 2) % (10**9 + 7)
        
        if n is even return (2^n - 2 - 2) % (10**9 + 7)
        
        
        1  2
        
        4  3
        
        1. all right
        
        4  1
         
        3  2
        
        2. all left
        
        2. 3
        
        1  4
        
        3. one pair
        
        2. 1
        
        3  4
        
        4. Other pair
        
        4. 3
        
        1. 2
        
        
        """
        return (pow(2, n, 10 ** 9 + 7) - 2) % (10 ** 9 + 7)