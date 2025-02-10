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
    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        For each i have the option to append it to previous element in cur if it makes a palendrome or add it to a new element. Only have option to add to new element if the previous is a palendrome

        s = "aab"
        self.res = []

        i = 0
        cur = []
            i = 1
            cur = ["a"]
                i = 2
                cur = ["aa"]
                    i = 3
                    cur = ["aab]

                    i = 3
                    cur = ["aa", "b"]

                i = 2
                cur = ["a", "a"]
                    i = 3
                    cur = ["a", "ab"]

                    i = 3
                    cur = ["a", "a", "b"]
        """

        self.res = []
        def helper(i, cur):
            if i == len(s):
                if cur[-1] == cur[-1][::-1]:
                    self.res.append(cur)
                return
            if not cur:
                helper(i+1, [s[i]])
            else:
                last = cur[-1]
                # If last element palendrome can add to prev, or to new
                helper(i+1, cur[:-1] + [cur[-1]+s[i]])
                if last == last[::-1]:
                    helper(i+1, cur + [s[i]])
                # If last element not palendrom can only add to prev
        
        helper(0, []) 

        return self.res