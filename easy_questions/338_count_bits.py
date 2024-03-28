
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Brute force for each number ranging from 0 to n inclusive, 
        Determine the number of 1 bits, and append to result arr

        """
        res = []

        def getCount(i):
            count = 0
            while i:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            return count

        for i in range(n+1):
            res.append(getCount(i))
        return res
