class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Iterate through
        if you see a 0, flip its and elements 2 to their opposite

        [1, 0, 0, 1, 0, 0]
        [1, 1, 1, 0, 0, 0]

        [0, 1, 1, 1]
        [1, 0, 0, 1]
        [1, 1, 1, 0]
        
        """
        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                for j in range(i+1, i + 3):
                    if nums[j] == 1:
                        nums[j] = 0
                    elif nums[j] == 0:
                        nums[j] = 1
                res += 1


        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return res
