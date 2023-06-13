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