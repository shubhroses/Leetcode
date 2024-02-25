class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        sliding window
        have a right pointer keep going
        maintain max and min
        and res
        if hit zero move left pointer

        [2, 3, -2, 4]
         l
                   r
        
        
        """
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMin)
        return res
