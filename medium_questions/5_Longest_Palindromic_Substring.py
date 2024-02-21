class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. Starting at every point assume it is the center of a palendromic string, 
            go out right and left until either side hits start or end of string.
            or characters are not the same
            return 
        2. Starting at every pair, do the same process

        """

        def helper(l, r, cur):
            # Return pal substr
            if l < 0 or r >= len(s):
                return cur
            
            if s[l] == s[r]:
                if l == r:
                    return helper(l-1, r+1, s[l])
                return helper(l-1, r+1, s[l] + cur + s[l])
            
            return cur
        
        res = ""
        for i in range(len(s)):
            oddLen = helper(i, i, "")
            evenLen = ""
            if i != len(s)-1:
                evenLen = helper(i, i+1, "")

            if len(oddLen) > len(res):
                res = oddLen
            if len(evenLen) > len(res):
                res = evenLen

        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Have a for loop for each i

        """
        res = s[0]

        for i in range(len(s)):
            # Odd length
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
            # Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
