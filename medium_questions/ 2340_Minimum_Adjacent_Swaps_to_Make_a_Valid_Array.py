class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        Go right to left to find min
        Go left to right to find max
        """
        minNum = min(nums)
        maxNum = max(nums)
        
        indexMin = -1
        indexMax = len(nums)
        
        for i in range(len(nums)):
            if(nums[i] == minNum):
                if(indexMin == -1):
                    indexMin = i
            if(nums[i] == maxNum):
                indexMax = i

        if(indexMin > indexMax):
            return (len(nums) - 1 - indexMax) + (indexMin) -1
        else:
            return (len(nums) - 1 - indexMax) + indexMin
        
        