class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Look at every subarray, if the sum is goal count += 1

        If the sum > goal: continue
        """
        counter = collections.Counter({0:1})
        res = s = 0
        for i in nums:
            s += i
            res += counter[s-goal]
            counter[s] += 1
        return res