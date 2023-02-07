class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1,1,2]
           i
             j


        """
        i, j = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            i+=1
            if j < len(nums):
                nums[i] = nums[j]
        return i