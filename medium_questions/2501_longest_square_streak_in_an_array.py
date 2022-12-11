class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        Consider every element as a start of a square streak
        
        [4,3,6,16,8,2]
         i
         
        res = 2
        
        curLen = 2
        
        """
        numsSet = set(nums)
        res = 1
        for i in range(len(nums)):
            curLen = 1
            cur = nums[i]
            while cur*cur in numsSet:
                curLen += 1
                cur = cur*cur
                res = max(res, curLen)
        if res == 1:
            return -1
        return res