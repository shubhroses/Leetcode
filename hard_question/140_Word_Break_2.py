class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Backtracking 
        
        
        """
        res = []
        def helper(curStr, curWord, i):
            if i >= len(s):
                if not curWord:
                    res.append(curStr)
                return
            if curWord + s[i] in wordDict:
                if not curStr:
                    helper(curWord + s[i], "", i +1)
                else:
                    helper(curStr + " " + curWord + s[i], "", i +1)
            helper(curStr, curWord + s[i], i+1)
            
        helper("","", 0)
        return res