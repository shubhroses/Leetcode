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