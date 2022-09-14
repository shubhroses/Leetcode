class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrone(s):
            i = 0
            j = len(s)-1
            res = True
            while i < j:
                if s[i] != s[j]:
                    res = False
                    break
                i+=1
                j-=1
            return res
        
        
        res = []
        part = []
        def helper(i):
            #base case
            if i >= len(s):
                res.append(part.copy())
                return
            
            #For each element after i, check that it is a palindrone
            for j in range(i, len(s)):
                if isPalindrone(s[i:j+1]):
                    #add substring to partition
                    part.append(s[i:j+1])
                    helper(j+1)
                    #Remove substring from partition
                    part.pop()
        helper(0)
        return res