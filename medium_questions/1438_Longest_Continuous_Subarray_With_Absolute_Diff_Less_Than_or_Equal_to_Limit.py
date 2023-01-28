class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Find longest subarray such that the absolute difference between any two elemets of this subarray is less than or equal to limit

        maintain a min heap and max heap

        Iterate through with right pointer
        keeping left pointer

        if maxheap[-1] - minheap[-1] > limit:
            pop from left 
        """

        maxLen, i = 0, 0
        minQueue, maxQueue = collections.deque([]), collections.deque([])
        for j in range(len(nums)):
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])
            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])
            
            if maxQueue[0] - minQueue[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return maxLen