class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        complement = number * all bits set
        """
        if n == 0:
            return 1
        numBits, num = 0, n

        while num > 0:
            numBits += 1
            num  = num >> 1
        
        allBits = 2**numBits - 1

        return n ^ allBits
