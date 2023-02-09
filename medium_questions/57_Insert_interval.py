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
