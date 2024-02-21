class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        s = "aba"
             l r

        res = 3

        """
        res = len(s)

        for i in range(len(s)):
            # Odd len
            l, r = i-1, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # Even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
