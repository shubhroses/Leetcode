class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        i = 0

        while i < len(nums):
            j = nums[i]

            if i < len(nums) and nums[i] != nums[j-1]:
                nums[i], nums[j-1] = nums[j-1], nums[i]
            else:
                i += 1

        for i, j in enumerate(nums):
            if i != j-1:
                res.append(i+1)
        return res