class Solution: 
    def getSmallestString(self, s: str) -> str: 
        saved = s
        for i in range(0, len(s)-1):
            l, r = s[i], s[i+1] 
            
            # both odd or even
            if (int(l) % 2 == 1 and int(r) % 2 == 1) or (int(l) % 2 == 0 and int(r) % 2 == 0):
                if int(r) < int(l):
                    saved = s[:i]
                    saved += s[i+1]
                    saved += s[i]
                    saved += s[i+2:]
                    break
        return saved

        # 100352_Lexicographically_Smallest_String_After_a_Swap.py
            
