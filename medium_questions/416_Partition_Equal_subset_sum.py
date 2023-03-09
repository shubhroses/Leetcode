class Solution:
    # Recursive
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot//2

        def helper(ind, curTot):
            if curTot == target:
                return True
            if ind == len(nums):
                return False
            
            take = helper(ind + 1, curTot + nums[ind])
            leave = helper(ind + 1, curTot)
            return take or leave
        
        return helper(0, 0)