class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        [-4, -1, 0, 3, 10]
          i             j
        """
        i, j = 0, len(nums)-1

        res = []
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                res.append(nums[i]**2)
                i+=1
            elif abs(nums[i]) < abs(nums[j]):
                res.append(nums[j]**2)
                j-=1
        return res[::-1]