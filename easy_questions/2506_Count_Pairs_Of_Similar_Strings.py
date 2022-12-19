class Solution:
    def similarPairs(self, words: List[str]) -> int:
        """
        For each word, convert to set, sort, add to wordSet
        """
        
        l = []
        
        for word in words:
            letterSet = set([c for c in word])
            letters = "".join(sorted(list(letterSet)))
            l.append(letters)
        
        
        count = 0
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] == l[j]:
                    count += 1
        return count