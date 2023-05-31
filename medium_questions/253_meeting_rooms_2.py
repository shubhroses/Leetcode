class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Any time there is an overlap increment count
        Any time a meeting ends decrement count
        Res is max that count ever was

        maintain min heap with end times, when current start is greater than min heap pop from heap

        1. Sort intervals
        2. 

        [[0,30],[5,10],[15,20]]
                  i

        heap: [30]

        res = 1

        if s < top heap:
            add e to heap
            update res
        while s > top heap:
            pop from heap 

        return res


        [[1,5],[8,9],[8,9]]
                s e
          
        res = 1
        heap = [5]
        """
        res = 1

        if not intervals:
            return 0

        intervals.sort(key = lambda x:x[0])

        heap = [intervals[0][1]]
        heapq.heapify(heap)

        for s, e in intervals[1:]:
            while heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            res = max(res, len(heap))


        return res


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        used_rooms = 0
        
        start_timings = sorted([i[0] for i in intervals])
        end_timing = sorted([i[1] for i in intervals])
        
        L = len(intervals)
        
        end_pointer = 0
        start_pointer = 0
        
        while start_pointer < L:
            if start_timings[start_pointer] >= end_timing[end_pointer]:
                used_rooms -=1
                end_pointer += 1
                
            used_rooms += 1
            start_pointer += 1
        return used_rooms
                
        
        if not intervals:
            return 0
        
        free_rooms = []

        intervals.sort(key= lambda x:x[0])
        
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)
        
        
        """
        Want to figure out the maximum number of overlap in times 
        
        1. sort by start time
        2. Iterate through, 
        
        [[0,30],[5,15],[10,20]]
          s1 e1  s2 e2
          
        if e1 > s2:
            count += 1
        
        [[9,10],[4,9],[4,17]]
        
        [4,17],[4,9], [9,10]
        
        
        """
        intervals.sort(key = lambda x:x[0])
        count = 1
        
        for i in range(len(intervals)-1):
            e1 = intervals[i][1]
            s2 = intervals[i+1][0]
            if e1 > s2:
                count += 1
                
        return count
    
    