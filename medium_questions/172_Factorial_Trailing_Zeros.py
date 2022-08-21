class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Want to count the number of times 5 is present 
        
        n=10
        c = 2
        
        """
        
        count = 0
        while n >= 5:
            c = n/5
            n/=5
            count+=int(c)
        return count