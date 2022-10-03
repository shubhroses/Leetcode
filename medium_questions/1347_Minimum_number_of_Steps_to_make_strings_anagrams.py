class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        cs: {b:2
            a:1}
            
        ct: {a:2
             b:1}
             
        go through each key k in cs:
            if cs[k] < ct[k]:
                count += ct[k]-cs[k]
        """
        cs = {}
        count = 0
        for c in s:
            cs[c] = cs.get(c, 0) + 1
        for c in t:
            if c in cs:
                if cs[c] == 0:
                    count += 1
                else:
                    cs[c] -= 1
            else:
                count += 1
        return count