class Solution:
    def numTrees(self, n: int) -> int:
        """
        
        """ 
        memo = {}
        def helper(s, e):
            if (s, e) in memo:
                return memo[(s,e)]
            if s == e:
                return 1
            res = 0
            for i in range(s, e+1):
                res += max(helper(s, i-1)*helper(i+1, e), helper(s, i-1),helper(i+1, e)) 
            memo[(s,e)] = res
            return res
            
            
        return helper(1, n)
        
    
        """
        helper(1, 3)
        
        i = 1           
        helper(1, 0) = 0
        helper(2, 3) = 1
            i = 2
            helper(2, 1) = 0
            helper(3, 3) = 1
            
            i = 3
            helper(3, 2) = 0
            helper(4, 3) = 0
        
        i = 2
        helper(1, 1) = 1
        helper(3, 3) = 1
        
        i = 3
        helper(1, 2) = 2
            i = 1
            helper(1, 0) = 0
            helper(2, 2) = 1
            i = 2
            helper(1, 1) = 1
            helper(2, 1) = 0
            
        helper(3, 2) = 0
        
        
        
        """