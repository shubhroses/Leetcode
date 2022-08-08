"""
Back Tracking Solution
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i):
            if i < 0:
                return 0
            return max(nums[i] + helper(i-2), helper(i-1))
        
        return helper(len(nums)-1)

"""
Back Tracking with Memoization
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            result = max(nums[i] + helper(i-2), helper(i-1))
            memo[i] = result
            return result
        
        
        return helper(len(nums)-1)



