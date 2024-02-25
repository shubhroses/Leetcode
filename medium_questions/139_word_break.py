class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Write helper function with l and r pointers
        if s[l:r+1] in word can take or leave
            take: l = r+1, r = r+1
            leave: l = l, r = r+1

             01234567
        s = "leetcode", wordDict = ["leet","code"]
                    l
                    r
        """
        memo = {}
        def inDict(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l == len(s):
                return True
            if r == len(s):
                return False
            take = False
            if s[l:r+1] in wordDict:
                take = inDict(r+1, r+1)
            leave = inDict(l, r+1)
            memo[(l, r)] = leave or take
            return memo[(l, r)]
        return inDict(0, 0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Write helper function with l and r pointers
        if s[l:r+1] in word can take or leave
            take: l = r+1, r = r+1
            leave: l = l, r = r+1

             01234567
        s = "leetcode", wordDict = ["leet","code"]
                    l
                    r
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
