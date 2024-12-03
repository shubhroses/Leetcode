class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        if nums[l] > nums[r]:

        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid -1

        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minInd = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if m != len(nums) - 1 and nums[m] > nums[m+1]:
                minInd = m + 1
                break
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        sortedNums = nums[minInd:] + nums[:minInd]

        l, r = 0, len(sortedNums) - 1
        while l <= r:
            m = (l + r) // 2
            if sortedNums[m] < target:
                l = m + 1
            elif sortedNums[m] > target:
                r = m - 1
            else:
                return (m + minInd) % len(nums)
        
        return -1
