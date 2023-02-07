class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextChar(str, ind):
            backspace_count = 0
            while ind >= 0:
                if str[ind] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -=1
                else:
                    break
                ind-=1
            return ind
        
        sp, tp = len(s)-1, len(t)-1 
        while sp >= 0 or tp>=0:
            i1 = nextChar(s, sp)
            i2 = nextChar(t, tp)

            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if s[i1] != t[i2]:
                return False
            sp = i1 - 1
            tp = i2 - 1
        return True
        
        
        
        
        
        """sStack, tStack = [], []

        for i, c in enumerate(s):
            if c == "#":
                if sStack:
                    sStack.pop()
            else:
                sStack.append(c)

        print(sStack)
        
        for i, c in enumerate(t):
            if c == "#":
                if tStack:
                    tStack.pop()
            else:
                tStack.append(c)
        
        if tStack == sStack:
            return True
        return False
        """
