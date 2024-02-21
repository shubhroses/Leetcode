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
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Do house robbers normally on nums[1:] and nums[:-1]

        Then take the max


        """
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def helper(i, canRob, dontRobLast):
            if (i, canRob, dontRobLast) in memo:
                return memo[(i, canRob, dontRobLast)]
            if dontRobLast:
                if i == len(nums)-1:
                    return 0
            elif i == len(nums):
                return 0
            
            rob = 0
            if canRob:
                rob = nums[i] + helper(i+1, False, dontRobLast)
            leave = helper(i+1, True, dontRobLast)

            memo[(i, canRob, dontRobLast)] = max(rob, leave)
            return memo[(i, canRob, dontRobLast)]
        
        return max(
            helper(i=0, canRob=True, dontRobLast=True),
            helper(i=1, canRob=True, dontRobLast=False)
        )
        

