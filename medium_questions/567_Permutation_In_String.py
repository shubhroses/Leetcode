class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Make a counter of s1 

        Go thorugh all windows in s2 of length len(s1)
        Maintain a counter, if counters are equal return True

        s1 = ab
             1234
        s2 = idba
              i
                r

        c1 = {a:1, b:1}
        c2 = {a:1, b:1}


        """
        c1 = {}
        for c in s1:
            c1[c] = c1.get(c, 0) + 1
        n = len(s1)
        
        c2 = {}
        for c in s2[:n]:
            c2[c] = c2.get(c, 0) + 1

        
        if c1 == c2:
            return True
        l = 0

        for r in range(n, len(s2)):
            c2[s2[r]] = c2.get(s2[r], 0) + 1
            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]
            l += 1
            if c1 == c2:
                return True
        return False
