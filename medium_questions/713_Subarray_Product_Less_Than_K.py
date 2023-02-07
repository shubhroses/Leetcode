class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        [10,5,2,6]
                l
                r

         k = 100
         res = 7
         curProd = 6
        """
        res = 0
        curProd = 1
        l = 0
        for r, n in enumerate(nums):
            curProd *= n
            while curProd >= k and l <= r:
                curProd /= nums[l]
                l+=1
            res += r-l+1
        return res