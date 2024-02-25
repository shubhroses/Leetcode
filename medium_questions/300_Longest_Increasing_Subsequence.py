class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #Top Down with memoization
        memo = {}
        def helper(i, mn):
            if i >= len(nums):
                return 0
            if (i, mn) in memo:
                return memo[(i, mn)]
            res = None
            if nums[i] > mn:
                res = max(helper(i+1, nums[i]) + 1, helper(i+1, mn))
            else:
                res = helper(i+1, mn)
            memo[(i, mn)] = res
            return res
        
        return helper(0, float("-inf"))

        #Bottom up with tabulation
        n = len(nums)
        dp = [1]*n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        """
        Helper(i, mn) returns length of longest increasing subsequence from 0-i
        
        base case: return helper(0, nums[0])
        
        if i >= len(nums):
            return 0
        
        if can take:
            return min(helper(i+1, nums[i]) + 1, helper(i+1, min))
        else:
            return helper(i+1, min)
        
        """
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Write helper function that returns length of longest increasing subseq

        if i > len(nums): return 0

        if nums[i] > prev: take or leave

        [0,1,0,3,2,3]
    p.   
                   i

        """
        memo = {}
        def length(prev, i):
            if (prev, i) in memo:
                return memo[(prev, i)]
            if i >= len(nums):
                return 0
            take = 0
            if nums[i] > prev:
                take = length(nums[i], i + 1) + 1
            leave = length(prev, i + 1)
            memo[(prev, i)] = max(take, leave)
            return memo[(prev, i)]

        return length(float("-inf"), 0)
        
