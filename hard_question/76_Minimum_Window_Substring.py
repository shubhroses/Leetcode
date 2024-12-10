class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        brute force. look at every substring of s and see if it contains all letters in t and return min
        m^2 * nlogm
        
        two pointers
        
        minArr = s
        minArr = s[i:j+1]
        
        t = "ABC"
             0123456789012
        s = "ADOBECODEBANC"
             i
             j
            
        minArr = "ADOBEC"
        
         
        d = {A:0, D:7, O:6, B:9, E:8, C:5} every letter in s and its index found in window 
        
        Since all letters in t are not in window, j+=1
        
        need function to check if all letters in t found in window.
        
        When all letters in t in window and length of window less than minArray, update minArray
        
        If s[j] in d: #update 
            s[j] = j
            
        When we encounter a duplicate letter, move the left pointer while all elements in t are still in s 
        
        
        t = aa
        
            01234567
        s = a
                i
                   j
             
        window = "CDEBA"
        c = {C:1, B:1, A:1}
        
        canRemoveIth = True
        
        minArray = CODEBANC
        
        
        t = aa
        window = 
                 i
        tCount = {A:1, B:1, C:1}
        windowCounter = {C:2, 0:1, D:1, E:1, B:1, A:1, N:1}
        """

        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
            
            
        def tInWindow(windowCounter):
            res = True
            
            for l,c in tCount.items():
                if windowCounter.get(l, 0) < c:
                    res = False     
            return res
        
        
        def canRemoveIth(windowCounter, i): 
            if tInWindow(windowCounter) and s[i] in tCount and windowCounter[s[i]] == tCount[s[i]]:
                return False
            return True
 
        minArr = s
        c = {} #{letter:count}
        i, j = 0, 0 
        
        while j < len(s):
            c[s[j]] = c.get(s[j], 0) + 1
            j+=1
            #window = s[i:j]
            
            if tInWindow(c):
                while canRemoveIth(c, i) and i < len(s):
                    c[s[i]] = c[s[i]]-1
                    if c[s[i]] <= 0:
                        del c[s[i]]
                    i+=1

                if j-i < len(minArr):
                    minArr = s[i:j]
          
        minCount = {}
        for c in minArr:
            minCount[c] = minCount.get(c, 0) + 1 
         
        if not tInWindow(minCount):
            return ""
        return minArr

        #Neet code solution

        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Create a counter for t

        Start with a window of len(t) in s, if all characters present, save window len

        if not all characters present, move window to right, leaving left
        if valid window, start popping from left until not valid 

        once not valid start adding to window again until valid and repeat process


             0123456789012
        s = "ADOBECODEBANC"
               l        r
             012
        t = "ABC"

        n = 3

        sW = {D:2, O:2, B:2, E:2, C:1, A:1}

        tW = {A:1, B:1, C:1}


        """
        def validWindow(sWindow, tWindow):
            for c, count in tWindow.items():
                if sWindow[c] < count:
                    return False
            return True

        tWindow = defaultdict(int)
        sWindow = defaultdict(int)

        n = len(t)
        for c in t:
            tWindow[c] += 1
        
        for c in s[:n]:
            sWindow[c] += 1
        
        if tWindow == sWindow:
            return s[:n]
        
        
        l = 0
        res = None
        for r in range(n,len(s)):
            sWindow[s[r]] += 1
            while validWindow(sWindow, tWindow):
                if not res or r-l+1 < len(res):
                    res = s[l:r+1]
                sWindow[s[l]] -= 1
                if sWindow[s[l]] == 0:
                    del sWindow[s[l]]
                l += 1
        if not res:
            return ""
        return res

        
            


        

