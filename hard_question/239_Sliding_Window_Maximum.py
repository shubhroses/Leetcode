import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        max heap with number and index 
        
        1. create heap from 0-k
        2. As we step through nums one my one
        3. Add new (element, index) to heap
        4. If top of heap now out of index, pop
        5. Append to res the top of heap
        """
        #Double ended queue
        
        n1 = [(-1*nums[i], i) for i in range(k)]
        heapq.heapify(n1)
        
        res = [-1*n1[0][0]]
        
        for i in range(k, len(nums)):
            heapq.heappush(n1, (-1*nums[i], i))
            topInd = n1[0][1]
            while topInd > i or topInd < i-k+1:
                heapq.heappop(n1)
                topInd = n1[0][1]
            res.append(-1*n1[0][0])
        return res

        #neetcode solution
        output = []
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            if(r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output