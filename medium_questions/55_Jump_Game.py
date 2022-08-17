class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Recursive with memoization
        memo = {}
        def helper(i):
            if i >= len(nums)-1:
                return True
            if i in memo:
                return memo[i]
            
            result = False
            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    result = True
                    break
            memo[i] = result
            return result
        return helper(0)

        # Iterative with memoization
        n = len(nums)
        dp = [0]*n
        dp[n-1] = 1 
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i]+1):
                if j+i < n and dp[j+i] == 1:
                    dp[i] = 1
                    break
        return dp[0]
        
        # Goal solution from neet code
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        return False

        #Working solutionmax_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x)
        
        
        
        
        
