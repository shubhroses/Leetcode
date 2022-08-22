class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1, 2, 3, 4]
                      
                         
        l =    [1, 1, 2, 6]
        
                      
        r =    [24, 12, 4, 1]
        """

        #Using n space
        n = len(nums)
        
        l = [1]*n
        for i in range(1, n):
            l[i] = l[i-1]*nums[i-1]
            
        r = [1]*n
        for i in range(n-2, -1, -1):
            r[i] = r[i+1]*nums[i+1]
            
        res = [l[i] * r[i] for i in range(n)]
        
        return res

        # Constant space
        n = len(nums)
        l = [1]*n
        
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        c = nums[-1]
        for i in range(n-2, -1, -1):
            l[i] = l[i] * c
            c *= nums[i]
            
        return l