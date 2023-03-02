class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        rangeStart, rangeEnd = 0, math.inf
        currentMaxNumber = -math.inf

        for arr in nums:
            heappush(minHeap, (arr[0], 0, arr))
            currentMaxNumber = max(currentMaxNumber, arr[0])
        
        while len(minHeap) == len(nums):
            num, i, arr = heappop(minHeap)
            if rangeEnd - rangeStart > currentMaxNumber - num:
                rangeStart = num
                rangeEnd = currentMaxNumber
            if len(arr) > i + 1:
                heappush(minHeap, (arr[i+1], i+1, arr))
                currentMaxNumber = max(currentMaxNumber, arr[i+1])
        return [rangeStart, rangeEnd]