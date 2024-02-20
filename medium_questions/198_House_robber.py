class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def helper(i, taken):
            if (i, taken) in memo:
                return memo[(i, taken)]
            if i == len(nums):
                return 0
            # Take
            if not taken:
                take = helper(i+1, True) + nums[i]
                skip = helper(i+1, False)
                memo[(i, taken)] = max(take, skip)
                return memo[(i, taken)]
            else:
                skip = helper(i+1, False)
                memo[(i, taken)] = skip
                return memo[(i, taken)]

            # Skip

        return helper(0, False)
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Have a helper function with variables i and can rob

        base case if i == len(nums):
            return 0
        
        Two scenario:
            if can rob:
                rob:
                dont rob
            if cant rob:
                dont rob
        return max of all options
        """
        memo = {}
        def helper(i, canRob):
            if (i, canRob) in memo:
                return memo[(i, canRob)]
            if i == len(nums):
                return 0
            
            rob = 0
            dontRob = 0
            if canRob:
                rob = nums[i] + helper(i+1, False)
            dontRob = helper(i+1, True)

            memo[(i, canRob)] = max(rob, dontRob)
            return memo[(i, canRob)]
        
        return helper(0, True)
