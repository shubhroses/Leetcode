class Solution:
    def minimumCost(self, s: str) -> int:
        if not s:
            return 0
        """
        Divide string into 2 
        """
        def helper(s1, s2, make):
            res1 = 0
        
            flipped = False
            for i in range(len(s1)-1, -1, -1):
                if s1[i] != make and not flipped or s1[i] == make and flipped:
                    res1 += i+1
                    flipped = not flipped
            

            res2 = 0
            flipped = False
            for i in range(len(s2)-1, -1, -1):
                if s2[i] != make and not flipped or s2[i] == make and flipped:
                    res2 += i+1
                    flipped = not flipped
            return res1 + res2
        
        
        n = len(s)
        s1 = s[:n//2]
        s2 = s[n//2:][::-1]
        
        return(min(helper(s1, s2, "1"), helper(s1, s2, "0")))