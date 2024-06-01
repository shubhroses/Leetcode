class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []

        i, start, end = 0, 0, 1

        # Skip all intervals that end before new start
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
            
        # Merge all intervals that overlap
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        # Add new interval
        merged.append(newInterval)


        # Add remaining intervals
        merged += intervals[i:]
        return merged


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        si ei 

        sn en 

        while sn > ei keep current intervals

        if sn between si and ei
            keep si
            keep max of en ei
        
        if si <= end of last element, update last element with max of cur and new last en
        
        [[1, 3], [4, 6]]  [2 , 5]
                  si ei  
        
        res = [[1, 5]]
        """

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
