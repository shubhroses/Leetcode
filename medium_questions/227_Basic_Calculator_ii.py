class Solution:
    def calculate(self, s: str) -> int:
        """
        1. Listen 
        
        2. Example
        
       
        
        - Remove all white spaces first
        - Have a helper function that
            Iterates thorugh the string
            if you see a multiplication symbol, or division symbol, do the operation and call function again
            base case, no + - * / in the string, return the number
        i. Find the * and /, do those operations first 
        
        s = "3 + 2 * 2" 
        
        1. s = 3+2*2
        2. s = 3+4
        3. s = 7
        
        ["3", "+", "2", "*", "2"]
               i
          
        new = []
        
        Problem: 13*2
        Start by converting string into alist of numbers and operations 
        """
        #Function to do arithmetic
        def arith(x, y, oper):
            x = int(x)
            y = int(y)
            if oper == "*":
                return x*y
            elif oper == "/":
                return x//y
            elif oper == "+":
                return x+y
            elif oper == "-":
                return x-y
        
        
        def helper(st):
            print(st)
            if len(st) <= 1:
                return st[0]
            new = []
            msInStr = "*" in st or "/" in st
            visited = set()
            if msInStr:
                for i in range(len(st)):
                    if st[i] == '*' or st[i] == '/':
                        result = arith(new[-1], st[i+1], st[i])
                        new[-1] = str(result)
                        visited.add(i+1)
                    elif i not in visited:
                        new.append(st[i])
            else:
                for i in range(len(st)):
                    if st[i] == '+' or st[i] == '-':
                        result = arith(new[-1], st[i+1], st[i])
                        new[-1] = str(result)
                        visited.add(i+1)
                    elif i not in visited:
                        new.append(st[i])
                        
            return helper(new)
            
                    
        #Remove all white spaces from s
        newS = ""
        for c in s:
            if c != ' ':
                newS += c
                
        #Put all numbers and characters into an array 
        newSArr = []
        start = 0
        for i in range(len(newS)):
            if newS[i] == "*" or newS[i] == "/" or newS[i] == "-" or newS[i] == "+":
                newSArr.append(newS[start:i])
                newSArr.append(newS[i])
                start = i+1
        newSArr.append(newS[start:])
                
        #Call helper function to get result in string form
        res = helper(newSArr)
        return int(res)

        # O(N), O(1) space complexity solution
        i = 0
        cur = prev = res = 0
        cur_operation = "+"
        
        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i +=1
                i -= 1
                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                else:
                    res -= prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif cur_char != " ":
                cur_operation = cur_char
            i+=1
        return res