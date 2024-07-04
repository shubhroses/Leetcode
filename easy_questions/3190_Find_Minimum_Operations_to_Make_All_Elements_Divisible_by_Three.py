class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        1, 2, 3, 4, 5, 6
        1  1  0  1  1  0
        if num is not divisible 3 increment count
        """

        res = 0
        for n in nums:
            if n % 3 != 0:
                res += 1
        return res

        

