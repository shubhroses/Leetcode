class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        if num & 1 == 1 then increment
        shift num down
        keep going until no n
        """
        res = 0
        while n:
            if n & 1 == 1:
                res += 1
            n  = n >> 1
        return res
