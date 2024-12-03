class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        l, r, m

        if m < r: rotation on left
        if l < m: rotation on right

        goal find position where m > m + 1
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if m != len(nums) - 1 and nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[0]
