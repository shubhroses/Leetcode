class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        i = 31
        while n:
            if n & 1 == 1:
                res += 2**i
            n = n >> 1
            i -= 1
        return res