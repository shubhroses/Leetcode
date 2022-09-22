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
            