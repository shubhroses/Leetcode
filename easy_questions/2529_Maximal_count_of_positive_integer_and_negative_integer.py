class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        numNeg = 0
        numPos = 0
        for num in nums:
            if num > 0:
                numPos += 1
            elif num < 0:
                numNeg += 1
        return max(numNeg, numPos)