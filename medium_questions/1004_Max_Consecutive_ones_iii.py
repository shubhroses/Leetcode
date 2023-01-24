class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find longest substring with only k zeros in it

        Look at every substring, maintaining count of zeros. 


        [1,1,1,0,0,0,1,1,1,1,0]
                   l
                   r 
         
        zeroCount = 3

        res = 5

        """
        zeroCount = 0
        res = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            if zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l+=1
            if zeroCount <= k:
                res = max(res, r-l+1)
        return res