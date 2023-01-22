class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        res = 0
        sign = 1
        for c in str(n):
            res += sign * int(c)
            sign *= -1
        return res