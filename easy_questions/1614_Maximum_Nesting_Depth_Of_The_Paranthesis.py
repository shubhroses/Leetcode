class Solution:
    def maxDepth(self, s: str) -> int:
        """
        maintain stack
        iterate through s
        
        every ( add to stack 
        every ) pop from stack
        
        maintain max stack size
        """
        
        count = 0
        res = 0
        
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            res = max(res, count)

        return res