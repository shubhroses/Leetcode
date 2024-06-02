class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. Sort by start time

        1.
        ----  ----

        2.
        ------
          -------

        3.
        -------------
          --------

        res = [s1, e1]

        s2 e2

        if e1 < s2:
            Add new interval to res
        if e1 >= s2:
            Change e1 to be max(e1, e2)
        """
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]

        for s2, e2 in intervals[1:]:
            e1 = res[-1][1]
            if e1 < s2:
                res.append([s2, e2])
            else:
                res[-1][1] = max(e1, e2)
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. Sort by start time
        2. Put first pair in result array
        3. if new start before or equal to previous end, 
            Update previous end to max of previous end and current end
        4. Otherwise put current pair in result
        

        [[1,3],[2,12],[8,10],[15,18]]
        
        [[1, 12]]


        [[1,4],[4,5]]

        [[1, 5]]
        """
        intervals.sort() # intervals.sort(key x: lambda x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res


