class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        dp = {0: 1}
        n = len(nums)
        acc = 0        
        for i in range(n):
            acc += nums[i]       
            key = acc % k
            
            if key in dp:
                res += dp[key]
                dp[key] += 1
            else:
                dp[key] = 1
            
        return res