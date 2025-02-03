class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        [1, 10][5, 15]
                s   e
         
        h = [10, 15] 
              t
        
        
        while heap and s >= h[-1]:
            popFromHeap
        if not heap or s <= h[-1]:
            add e to heap
        if size of heap > cur max:
            earliestStart = s
        
        max = size of heap 
        earliest year is s
        
        1. sort by start time
        2. Itertate through logs maintaining heap
        3. If s < top of heap
        4.  Add e to heap
        5.  If size of heap is new max, save start time as earliest year with maximum population
        
        [1, 10][3, 6][6, 10]
                      s  e
         
         h = [10, 10]
         
         curMax = 2
         earlistStart = 3
        """
        # sorting
        logs.sort(key = lambda x:x[0])
        
        heap = []
        curMax = 0
        earliest = logs[0][0]
        
        for s, e in logs:
            while heap and s >= heap[0]:
                heapq.heappop(heap)
            if not heap or s < heap[0]:
                heapq.heappush(heap, e)
            if len(heap) > curMax:
                earliest = s
                curMax = len(heap)
        return earliest
    
        """
        [[1950,1961],[1960,1971],[1970,1981]]
                                    s   e
        
        heap = [1971, 1981]
        curMax = 2
        earliest = 1960
        """
        """
        nlogn 
        """