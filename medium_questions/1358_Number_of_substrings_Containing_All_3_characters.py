class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Look at every substring and determine if it contains all 3 characters

        
        """
        a = b = c = 0

        ans, i, n = 0, 0, len(s)

        for j, letter in enumerate(s):
            if letter == 'a':
                a += 1
            elif letter == 'b':
                b += 1
            elif letter == 'c':
                c += 1
            while a > 0 and b > 0 and c > 0:
                ans += n-j
                if s[i] == 'a':
                    a -=1
                elif s[i] == 'b':
                    b -=1
                elif s[i] == 'c':
                    c -=1
                i += 1
        return ans