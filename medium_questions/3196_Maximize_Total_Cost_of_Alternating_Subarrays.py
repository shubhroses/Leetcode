from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def helper(i, pos):
            if i == n:
                return 0
            if (i, pos) in memo:
                return memo[(i, pos)]
            # Calculate the cost if we stop the subarray here
            stop = (pos * nums[i]) + helper(i + 1, 1)
            # Calculate the cost if we continue the subarray
            cont = (pos * nums[i]) + helper(i + 1, -pos)

            memo[(i, pos)] = max(stop, cont)
            return memo[(i, pos)]

        # Initialize the recursion
        return helper(0, 1)

        

