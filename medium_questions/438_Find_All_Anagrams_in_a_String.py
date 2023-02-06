class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cPattern = {}
        for c in p:
            cPattern[c] = cPattern.get(c, 0) + 1
        
        n = len(p)

        cString = {}
        for c in s[:n]:
            cString[c] = cString.get(c, 0) + 1

        res = []

        if cPattern == cString:
            res.append(0)
        
        l = 0
        for r in range(n, len(s)):
            cString[s[r]] = cString.get(s[r], 0) + 1
            cString[s[l]] -= 1
            if cString[s[l]] == 0:
                del cString[s[l]]
            l+=1
            if cString == cPattern:
                res.append(l)
        return res