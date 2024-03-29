class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        """
        1. Convert all negative numbers to zero
        2. For each element in nums, if the value in inbounds, mark that this value exists by converting the element at that index to negative if it is positive
            If it is zero make it negative with value greater than len of array
        3. Iterate through array and if positive it does not appear
        """
        

        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        
        for i in range(len(A)):
            val = abs(A[i])
            
            if 1 <= val <= len(A):
                if A[val-1] > 0:
                    A[val-1] *= -1
                elif A[val-1] == 0:
                    A[val-1] = -1 * (len(A) +1)
        for i in range(1, len(A)+1):
            if A[i-1] >= 0:
                return i
            
        return len(A)+1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1