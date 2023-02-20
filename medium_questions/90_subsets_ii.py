class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        res.append([])
        startIndex, endIndex = 0, 0
        for i in range(len(nums)):
            startIndex = 0
            if i > 0 and nums[i] == nums[i-1]:
                startIndex = endIndex + 1
            endIndex = len(res)-1

            for j in range(startIndex, endIndex + 1):
                temp = list(res[j])
                temp.append(nums[i])
                res.append(temp)
        return res