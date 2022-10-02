class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        c = 0
        
        def binarySearch(i, l, r):
            res = 0
            while l < r:
                if nums[r] + nums[l] > nums[i]:
                    res += r-l
                    r -=1
                else:
                    l += 1
            return res

        n = len(nums)
        nums.sort()
        
        for i in range(n-1, 1, -1):
            c += binarySearch(i, 0, i-1)
        return c