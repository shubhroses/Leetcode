class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        """
        s = dart
        n = 4

        k = 3

        nextLetter = (i + k) % n

        0 + 3 = 3 % 4 = 3
        """
        n = len(s)
        res = ""
        for i in range(n):
            res += s[(i+k)%n]
        return res

        
