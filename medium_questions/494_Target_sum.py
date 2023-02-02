class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        At each index we can add or subtract that value to total

        base case:
            If current total equals target return 1

        add current value to current total and re call function
        subtract current value to current total and re call function

        Save index & value
        """
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[target]


        dp = {}
        def helper(ind, curTotal):
            if (ind, curTotal) in dp:
                return dp[(ind, curTotal)]
            if curTotal == target and ind == len(nums):
                return 1
            if ind == len(nums):
                return 0
            dp[(ind, curTotal)] = helper(ind+1, curTotal + nums[ind]) + helper(ind+1, curTotal - nums[ind])
            return dp[(ind, curTotal)]

        return helper(0, 0)