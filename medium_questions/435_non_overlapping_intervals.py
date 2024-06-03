class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Iterate through intervals in order
        Determine if there is an overlap, remove the one that ends later
        Maintain count


        1. Sort intervals by start time
        2. If current start before previous end, increment count, update previous end to be min(of current end, last end)


        [[1,2], [1,3],[2,3],[3,4]]
        prevEnd = 2



        """
        res = 0

        intervals.sort()
        prevEnd =intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
                continue
            prevEnd =  intervals[i][1]
        return res
