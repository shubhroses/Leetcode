class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            j = nums[i] - 1 
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        res = []

        for i, n in enumerate(nums):
            if i != n-1:
                res.append(n)
        return res