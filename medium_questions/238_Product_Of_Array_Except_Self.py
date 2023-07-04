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
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1, 2, 3, 4]
                      i
        left = [1, 1, 2, 6]

        right= [24, 12, 4, 1]

        result = [24, 12, 8, 6]
        """
        left = [1]
        for i in range(1, len(nums)):
            left.append(nums[i-1] * left[-1])

        right = [1]
        for i in range(len(nums)-2, -1, -1):
            right.append(nums[i+1] * right[-1])
        right = right[::-1]

        res = []
        for i in range(len(left)):
            res.append(left[i]*right[i])

        return res
        