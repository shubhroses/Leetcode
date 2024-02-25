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
    
class Solution:
    # Memo
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot//2

        memo = [[-1 for x in range(target + 1)] for y in range(len(nums))]

        def helper(ind, curTot):
            if curTot == target:
                return 1 
            if ind == len(nums) or curTot > target:
                return 0
            if memo[ind][curTot] == -1:
                if helper(ind + 1, curTot + nums[ind]):
                    memo[ind][curTot] = 1
                    return 1
                memo[ind][curTot] = helper(ind + 1, curTot)
            return memo[ind][curTot]
        
        return True if helper(0, 0) == 1 else False
    
    

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s//2

        n = len(nums)

        memo = [[False for x in range(s + 1)] for y in range(n)]

        for i in range(n):
            memo[i][0] = True

        for j in range(1, s+1):
            memo[0][j] = nums[0] == j

        for i in range(1, n):
            for j in range(1, s+1):
                if memo[i-1][j]:
                   memo[i][j] = memo[i-1][j]
                elif j >= nums[i]:
                    memo[i][j] = memo[i-1][j-nums[i]]

        return memo[n-1][s]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot//2
        memo = {}
        def helper(i, cur):
            if (i, cur) in memo:
                return memo[(i, cur)]
            if cur == target:
                return True
            if cur > target or i >= len(nums):
                return False
            take = helper(i+1, cur + nums[i])
            leave = helper(i+1, cur)
            if take or leave:
                memo[(i, cur)] = True
            else:
                memo[(i, cur)] = False
            return memo[(i, cur)]
        return helper(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot//2
        dp = set()
        dp.add(0)


        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
