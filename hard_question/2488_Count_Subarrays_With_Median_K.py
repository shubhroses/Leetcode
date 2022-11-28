class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Need to find the median of every sub array 
        
        
        Brute force
            Look at every subarray 
            Determine median
            If median == k: increment count 
            
        [3,2,1,4,5]  
         i
           j
           
       [1, 2, 3, 4]
    
       len(subarray) = 4 // 2 = 2
       
        How to remove sorting 
        
        How to find median of unsorted array 
        
        [1 2 3 4 5]
       
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArray = nums[i:j+1]
                """
                Use quick select to find the len(subArray)//2 largest element in subArray 
                
                """
        return res