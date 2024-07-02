class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n//2):
            avg = (nums[i] + nums[n-i-1]) / 2
            res = min(res, avg)
        return res
