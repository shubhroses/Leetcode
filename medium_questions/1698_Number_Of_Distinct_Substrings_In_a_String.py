class Solution:
    def countDistinct(self, s: str) -> int:
        trie = {}
        res = 0
        for i in range(len(s)):
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur:
                    cur[s[j]] = {}
                    res +=1
                cur = cur[s[j]]
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        1. create a dictionary to store the trie
        
        If current substring is not in prefix add a new trie
        If it is a prefix but does nt assear as a string
        
        """
        
        trie, res = dict(), 0
        for i in range(len(s)):
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur:
                    cur[s[j]] = dict()
                    res +=1
                cur = cur[s[j]]
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        use two for loops to get every substring
        save substring in set
        return size of set
        
        n2 
        n2
        """
        
        saved = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                saved.add(substr)
        return len(saved)
        """
        aabbaa
        
        """