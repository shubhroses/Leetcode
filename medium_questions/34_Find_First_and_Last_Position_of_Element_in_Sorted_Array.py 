class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        First = find first instance of target
        Find the first instance of a target
        """
        if not nums:
            return [-1, -1]
        first = -1
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2
            if nums[m] >= target:
                r = m-1
                first = m
            else:
                l = m+1
        last = -1
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2
            if nums[m] <= target:
                l = m+1
                last = m
            else:
                r = m-1
        if nums[first]!= target:
            return [-1, -1]
        return [first, last]