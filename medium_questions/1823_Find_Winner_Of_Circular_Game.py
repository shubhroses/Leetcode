class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Brute force:
        
        k = 6
        n = 5
        
        delete k%n = 1
        
        n = [3, 5]
        k = 2
        
        cur = 0
        index = (k + cur) % len(n) - 1 => 2 % 5 - 1 = 1
        
        cur = 1
        index = (2 + 1) % 4 - 1 => 2
        
        cur = 2
        index = (2 + 2) % 3 - 1 => 0
        
        
        
        """
        nums = [i+1 for i in range(n)]
        
        cur = 0
        while len(nums) > 1:
            index = (k + cur - 1) % len(nums)
            nums = nums[:index] + nums[index+1:]
            cur = index
        return nums[0]