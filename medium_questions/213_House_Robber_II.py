class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Run house robber on nums[1:] and nums[:-1] to return max

        ind and canRob

        if reach end of nums:
            return 0

        if canRob:
            helper(ind+1, cantrob) + nums[ind]
        skip
        helper(ind+1, canrob)



        """
        if len(nums) == 1:
            return nums[0]
        dp = {}
        def helper(i, canRob, arr):
            if (i, canRob, tuple(arr)) in dp:
                return dp[(i, canRob, tuple(arr))]
            if i == len(arr):
                return 0
            if canRob:
                rob = helper(i+1, False, arr) + arr[i]
                dontRob = helper(i+1, True, arr)
                dp[(i, canRob, tuple(arr))] = max(rob, dontRob)
                return dp[(i, canRob, tuple(arr))]
            dontRob = helper(i+1, True, arr)
            dp[(i, canRob, tuple(arr))] = dontRob
            return dp[(i, canRob, tuple(arr))]

        return max(helper(0, True, nums[1:]), helper(0, True, nums[:-1]))