class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        m = {}
        totalK = 0 # total pairs found in n[l:r]
        goodSub = 0
        while r < len(nums):
            if nums[r] in m:
                m[nums[r]] += 1
                totalK += m[nums[r]] - 1 # counting pairs 
            else:
                m[nums[r]] = 1
            while totalK >= k: # we found k pairs in nums[l:r] we don't need to calculate ahead
                goodSub += len(nums) - r # calculate good subarray which is just the number of subarrays you can get adding remaining n - r elements
                m[nums[l]] -= 1
                totalK -= m[nums[l]] # updating pairs because window is going to be reduced
                l += 1 # window reduced
            r += 1
        return goodSub  