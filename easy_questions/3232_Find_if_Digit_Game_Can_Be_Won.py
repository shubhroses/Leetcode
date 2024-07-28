class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0
        doubleSum = 0

        for n in nums:
            if len(str(n)) > 1:
                doubleSum += n
            else:
                singleSum += n
        
        if singleSum == doubleSum:
            return False
        return True
