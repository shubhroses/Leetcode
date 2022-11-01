class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        Need to go all the way down 
        
        Easy to do brute force 
        
        1*1 + 4*2 + 6*3 + 4*4 + 1*5 
        
        Slides must have slide number:
        Start with an agenda, summary of the discussion
        
        """  
        result = 0
        m = len(nums) - 1
        mCk = 1
        for k, num in enumerate(nums):
            result = (result + mCk * num) % 10
            mCk *= m - k
            mCk //= k + 1
        return result

        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1])%10
            nums.pop()
        return nums[0]