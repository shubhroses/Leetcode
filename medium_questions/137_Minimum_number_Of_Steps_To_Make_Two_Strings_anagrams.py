class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        1. Create counter form strings t and s
        2. 
        """
        count = 0
        
        sCount = {}
        for c in s:
            sCount[c] = sCount.get(c, 0) + 1
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
            
        res = 0
        
        for letter, count in sCount.items():
            res += max(count - tCount.get(letter, 0), 0)
        return res