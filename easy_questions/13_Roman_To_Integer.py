class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        labels = {}
        labels[len(s)-1] = False
        for i in range(len(s)-2, -1, -1):
            if mp[s[i]] < mp[s[i+1]]:
                labels[i] = True
            else:
                labels[i] = False

        res = 0
        for i, c in enumerate(s):
            if labels[i] == True:
                res -= mp[c]
            else:
                res += mp[c]
        return res