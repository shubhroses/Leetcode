class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        s = "coaching", t = "coding"
               i               j
                             012345
        Two pointer 
        
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
        return len(t) - j
        
        
        s = "abcde", t = "a"
              i            j
              
              
        s = "z", t = "abcde"
              i       j
          5 - 0 = 5
         
        """
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j