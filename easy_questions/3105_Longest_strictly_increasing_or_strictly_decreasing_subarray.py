class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        hasBeenIncreasing = False
        hasBeenDecreasing = False
        """
        hasBeenIncreasing = False
        hasBeenDecreasing = False

        cur = res = 0
        for i in range(len(nums)-1):
            l, r = nums[i], nums[i+1]
            # Increasing
            if l < r:
                if hasBeenIncreasing:
                    cur += 1
                else:
                    cur = 2
                hasBeenIncreasing = True
                hasBeenDecreasing = False
            elif l > r: # Decreasing
                if hasBeenDecreasing:
                    cur += 1
                else:
                    cur = 2
                hasBeenIncreasing = False
                hasBeenDecreasing = True
            else:
                hasBeenIncreasing = False
                hasBeenDecreasing = False
                cur = 1
            res = max(res, cur)
        return max(res, 1)

        # 3105_Longest_strictly_increasing_or_strictly_decreasing_subarray.py