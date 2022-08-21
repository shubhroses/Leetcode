class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            
            num = str(n)
            temp = 0
            for ch in num:
                temp += int(ch)**2
            n = temp
            
        return True