class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
            
        return 0 if res == float("inf") else res

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
         0,1,2,3,4,5,6
        [2,3,1,2,4,3]
                   l
                     r

        curSum = 3
        target = 7
        res = 3
        """
        l = 0
        r = 0
        curSum = 0
        res = float("inf")
        while r <= len(nums) and l <= len(nums):
            if curSum >= target: # move left
                res = min(res, r-l)
                curSum -= nums[l]
                l += 1
            else: # move right
                if r == len(nums):
                    break
                curSum += nums[r]
                r += 1
        if res == float("inf"):
            return 0
        return res