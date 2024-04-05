class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Do the swapping again and if the 
        """
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        print(nums)
        
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)
        
        
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = 0
        for n in nums:
            cur = cur ^ n
        
        for i in range(len(nums)+1):
            cur = cur ^ i
        
        return cur