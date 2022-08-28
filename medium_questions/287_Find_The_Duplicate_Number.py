class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Brute force: sort , iterate through once comparing ajacent elements
        nlogn
        
        1 + 2 + 3 + 4 + ... + n + (x)
        
        take sum of nums, take 1 + ... + n, subtract and we have n 
        
        [1, 3, 4, 2, 2]
        to_n = 1 + 2 + 3 + 4 = 10
        
        tot = 12 
        
        return 12-10 = 2
        
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow