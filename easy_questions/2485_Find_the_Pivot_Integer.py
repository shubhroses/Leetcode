class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Take sum of everything

        1, 2, 3, 4, 5, 6, 7, 8
                       i
        
        (8*9)/2 = 36 
        
        left = 21
        right = 
        
        right = 36 - 21 + 6 = 21
        
        8*9 = 72 / 2 = 36
        
        total = 36
        res = -1
        
        n = 1
        total = 1
        res = -1
        
        1
        i
        left = 1
        right = 1-1+1 = 1
        
        
        1 2 3 4
            i
        
        total = 10
        left = 6
        right = 10 - 6 + 3 = 7
        
        
        """
        total = ((n+1)*(n))/2
        res = -1
        for i in range(1, n+1):
            left = ((i+1)*(i))/2
            right = total - left + i
            if left == right:
                res = i
        return res