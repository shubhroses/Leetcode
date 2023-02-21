class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [-1,0,3,5,9,12]
         l    lr     r
         0. 1 2 3 4  5

         target = 4

         m = r-l//2 = 2 
        """

        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2 
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return -1