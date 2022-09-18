class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        abbd
         i
         
        ac
        
        k = 2
        [i:i+k]
        
        n^2
        
        c = {a:1
             b:2
             d:1
        }
        len(s) = 4
        k = 2
        4-2 = 2
        
        abbd
           i
        substr = ab
        """

        stack = [['#', 0]] #Character and count
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join(c*k for c,k in stack)
        
        
        
        length = -1
        while length != len(s):
            length = len(s)
            count = 1
            for i in range(len(s)):
                count += 1
                if i == 0 or s[i] != s[i-1]:
                    count = 1
                elif count == k:
                    s = s[:i-k] + s[k:]
                    break
        return s