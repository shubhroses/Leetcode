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