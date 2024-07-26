class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)-1):
            l, r = nums[i], nums[i+1]
            if l%2 == r%2:
                return False
        return True

        