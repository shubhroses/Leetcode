class Solution:
    def decodeString(self, s: str) -> str:
        """
        0123
        20[b]
          i j
        
        i = 0
        j = 3
        
        curNum = "20"
        
        def helper(substr):
            
        1. Get the number
        2. Every time you see an open paranthesis call recursive function
        3. 
        
        substr = 20[b]
        
        substr = b
        if substr does not contain brackets just return substring 
        
        
        s = "20[b]"
               i
        i = 0
        curNum = "20"
        while not isDigit(s[i]):
            curNum += i
            i += 1
        if s[i] == '[':
            helper(s[i:])
            
        """
        

        
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[': 
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString
    
        """
        1. [
            add current string and current number to stack, reset each
        2. ]
            Get number and prev string from stack, calculate new curString
        3. digit
            Update curNumber
        4. alphabet
            Update curString
        
        
        
        """
        
        """
        3[a2[c]]
               c
        
        stack = ['', 3]
        curNum = 0
        curString = 'acc'
        
        num = 2
        prevString = 'a'
        """
        
        
        
        
        """
        s = 3[a2[c]]
                  c
                  
      cur = cc
        curNUm = 3, curStr = "a"
        
        curStr = acc
    
        res = ""
        curNum = "2"
        curStr = "c"
        
        stack = [[3, "a"]]
        
        if c = ] pop from stack 
        
        """