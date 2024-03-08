class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        If two characters a different have following options

        insert on w1

        delete on w1 

        replace on w1
        """
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1) and j >= len(word2):
                return 0
            elif i >= len(word1):
                return helper(i, j+1) + 1
            elif j >= len(word2):
                return helper(i+1, j) + 1
            
            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            insert = helper(i, j+1) + 1
            delete = helper(i+1, j) + 1
            replace = helper(i+1, j+1) + 1
            memo[(i, j)] = min(insert, delete, replace) 
            return memo[(i, j)]

        return helper(0, 0)
