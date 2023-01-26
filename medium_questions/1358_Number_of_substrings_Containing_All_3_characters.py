class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Look at every substring and determine if it contains all 3 characters

        
        """
        a = b = c = 0

        ans, l, n = 0, 0, len(s)

        for r, letter in enumerate(s):
            if letter == 'a':
                a += 1
            elif letter == 'b':
                b += 1
            elif letter == 'c':
                c += 1
            while a > 0 and b > 0 and c > 0:
                ans += n-r
                if s[l] == 'a':
                    a -=1
                elif s[l] == 'b':
                    b -=1
                elif s[l] == 'c':
                    c -=1
                l += 1
        return ans