class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        memo = {}
        def helper(ind, prevI, prevD):
            if (ind, prevI, prevD) in memo:
                return memo[(ind, prevI, prevD)]
            if ind == len(nums):
                return 1
            
            res = 0
            for curI in range(prevI, nums[ind]+1):
                curD = nums[ind] - curI
                if prevI <= curI and prevD >= curD:
                    res += helper(ind + 1, curI, curD)
            memo[(ind, prevI, prevD)] = res % MOD
            return memo[(ind, prevI, prevD)]
        
        
        return helper(0, 0, float("inf"))